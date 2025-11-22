"""
Basic Deepchecks data integrity checks.
"""
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import full_suite
import pandas as pd


def run_deepchecks(path='data/data.csv', out='reports/deepchecks_report.html'):
    df = pd.read_csv(path)
    target = 'target'
    X = df.drop(columns=[target])
    y = df[target]

    dataset = Dataset(df, label=target)

    suite = full_suite()
    results = suite.run(dataset)

    os.makedirs('reports', exist_ok=True)
    results.save_as_html(out)
    print('Deepchecks report saved to', out)

if __name__ == '__main__':
    import os
    run_deepchecks()
