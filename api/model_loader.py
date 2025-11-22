import os
from joblib import load

MODEL_PATH = os.environ.get('MODEL_PATH', 'artifacts/model.joblib')

_model = None

def load_model():
    global _model
    if _model is None:
        _model = load(MODEL_PATH)
    return _model
