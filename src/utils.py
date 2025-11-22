import joblib
import os
from sklearn.model_selection import train_test_split
import pandas as pd


def load_data(path='data/data.csv'):
    df = pd.read_csv(path)
    X = df.drop(columns=['target'])
    y = df['target']
    return train_test_split(X, y, test_size=0.2, random_state=42)


def save_model(model, path='artifacts/model.joblib'):
    import joblib, os
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)


def load_model(path='artifacts/model.joblib'):
    return joblib.load(path)
