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
onnx_classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
nlp = spacy.load("en_core_web_sm")


class Response(BaseModel):
    id: str = 0
    sentence: str
    label: str
    score: float


@app.get("/predict_subjectivity", response_model=Response)
def predict_subjectivity(sentence: str):
    result = onnx_classifier(sentence)[0]
    return {"label": result["label"],
            "sentence": sentence,
            "score": result["score"]}


@app.get("/predict_subjectivity_on_texts", response_model=List[Response])
def predict_subjectivity(paragraph: str):
    doc = nlp(paragraph)

    results = []
    for sent_id, sentence in enumerate(doc.sents):
        result = onnx_classifier(sentence.text)[0]
        results.append({
            "id": sent_id,
            "sentence": sentence.text,
            "label": result["label"],
            "score": result["score"]
        })
    return results
