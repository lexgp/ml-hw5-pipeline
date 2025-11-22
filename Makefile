.PHONY: data train run api clean

data:
	python src/generate_data.py

train:
	python src/train.py

api:
	uvicorn api.main:app --reload --host 0.0.0.0 --port 8080

clean:
	rm -rf artifacts mlruns reports
