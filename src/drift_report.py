"""
Создаёт report по дрейфу данных через Evidently
"""
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import os


def make_report(reference_path='data/data.csv', current_path=None, out='reports/evidently_drift.html'):
    df_ref = pd.read_csv(reference_path)
    if current_path is None:
        # для простоты используем ту же выборку, можно модифицировать для имитации дрейфа
        df_curr = df_ref.sample(frac=0.8, random_state=1).reset_index(drop=True)
    else:
        df_curr = pd.read_csv(current_path)

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=df_ref, current_data=df_curr)

    os.makedirs('reports', exist_ok=True)
    report.save_html(out)
    print('Evidently report saved to', out)

if __name__ == '__main__':
    make_report()
