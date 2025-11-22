CI notes:
- MLflow в CI использует локальную директорию mlruns — при необходимости сохраняйте артефакты отдельно
- Для связки с внешним MLflow Tracking Server можно настроить переменную MLFLOW_TRACKING_URI
- В GitHub Actions можно сохранять артефакты при помощи actions/upload-artifact
