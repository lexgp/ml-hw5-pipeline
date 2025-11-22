"""
Обучение модели с логированием в MLflow.
"""
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from utils import load_data, save_model
import numpy as np
import os

os.makedirs('artifacts', exist_ok=True)

X_train, X_test, y_train, y_test = load_data()

with mlflow.start_run():
    params = {"n_estimators": 100, "random_state": 42}
    mlflow.log_params(params)

    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    mlflow.log_metric('accuracy', float(acc))

    # save model both as artifact and as joblib for API
    input_example = X_test[:1]
    mlflow.sklearn.log_model(model, name='model', input_example=input_example)
    save_model(model, path='artifacts/model.joblib')

    print('Accuracy:', acc)
