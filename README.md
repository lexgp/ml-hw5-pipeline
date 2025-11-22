## Локальный запуск проекта

## 1. Клонировать репозиторий

```bash
git clone git@github.com:lexgp/ml-hw5-pipeline.git
cd ml-hw5-pipeline
```

## 2. Создать виртуальное окружение и установить зависимости

```bash
# python3.9 -m venv ./venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Сгенерировать данные и обучить модель

```bash
python src/generate_data.py
python src/train.py
```

## 4. Запустить MLflow UI

```bash
mlflow ui --port 5000
# открыть http://localhost:5000
```

## 5. Запустить API (локально)

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8080
```

---

## 6. Поспользоваться методом predict

POST `http://127.0.0.1:8080/docs#/default/predict_predict_post`

```json
{
  "features": {
    "feature_0": -0.5293321124483709,
    "feature_1": -0.09338685889994829,
    "feature_2": -1.5265723617342744,
    "feature_3": 0.40684650400043243,
    "feature_4": -0.6196994641009175
  }
}
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "features": {
    "feature_0": -0.5293321124483709,
    "feature_1": -0.09338685889994829,
    "feature_2": -1.5265723617342744,
    "feature_3": 0.40684650400043243,
    "feature_4": -0.6196994641009175
  }
}'
```

### Дополнительно:
- Последовательность: `generate_data.py` -> `train.py` -> `artifacts/model.joblib`.
- Deepchecks и Evidently сохраняют отчёты в `reports/`.
- MLflow GUI доступен через `mlflow ui` и покажет зарегистрированные параметры/метрики/модель.
