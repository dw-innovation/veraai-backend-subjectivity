from pydantic import BaseModel, validator
import spacy
from typing import List
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = ORTModelForSequenceClassification.from_pretrained('model', file_name='model.onnx',
                                                          num_labels=2,
                                                          id2label={0: "Not-subjective", 1: "Subjective"},
                                                          label2id={"Not-subjective": 1, "Subjective": 0}
                                                          )
tokenizer = AutoTokenizer.from_pretrained('model')
onnx_classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, truncation=True)
nlp = spacy.load("xx_ent_wiki_sm")
nlp.add_pipe('sentencizer')


class Response(BaseModel):
    id: str = 0
    sentence: str
    label: str
    score: float
    start_index: int
    end_index: int

class Paragraph(BaseModel):
    paragraph: str


@app.get("/predict_subjectivity", response_model=Response)
def predict_subjectivity(sentence: str):
    result = onnx_classifier(sentence)[0]
    return {"label": result["label"],
            "sentence": sentence,
            "score": result["score"]}


@app.post("/predict_subjectivity_on_texts", response_model=List[Response])
def predict_subjectivity(body: Paragraph):
    doc = nlp(body.paragraph)

    results = []
    for sent_id, sentence in enumerate(doc.sents):
        result = onnx_classifier(sentence.text)[0]
        results.append({
            "id": sent_id,
            "start_index": sentence.start_char,
            "end_index": sentence.end_char,
            "sentence": sentence.text,
            "label": result["label"],
            "score": result["score"]
        })
    return results
