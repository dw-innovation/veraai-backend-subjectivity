from pydantic import BaseModel, validator
import os
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

model = ORTModelForSequenceClassification.from_pretrained('model', file_name='model.onnx')
tokenizer = AutoTokenizer.from_pretrained('model')
onnx_classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)


class Response(BaseModel):
    label: str
    score: float


@app.post("/predict_subjectivity", response_model=Response)
def predict_subjectivity(sentence: str):
    result = onnx_classifier(sentence)[0]
    return {"label": result["label"],
            "score": result["score"]}
