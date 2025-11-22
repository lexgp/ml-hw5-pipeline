from fastapi import FastAPI
from pydantic import BaseModel
from api.model_loader import load_model
import pandas as pd

app = FastAPI(title='ml-hw5-pipeline API')

class PredictRequest(BaseModel):
    features: dict

class PredictResponse(BaseModel):
    prediction: int

@app.get('/')
def root():
    return {'status': 'ok'}

@app.post('/predict', response_model=PredictResponse)
def predict(req: PredictRequest):
    model = load_model()
    # features must be dict {'feature_0': val, ...}
    df = pd.DataFrame([req.features])
    pred = model.predict(df)[0]
    return {'prediction': int(pred)}
