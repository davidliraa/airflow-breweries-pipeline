from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os
import glob

def aggregate_breweries():
    input_dir = '/opt/airflow/data_lake/silver/breweries'
    output_dir = '/opt/airflow/data_lake/gold/breweries'
    os.makedirs(output_dir, exist_ok=True)

    # Pega todos os arquivos CSV da camada silver
    csv_files = glob.glob(os.path.join(input_dir, 'breweries_silver_*.csv'))
    if not csv_files:
        raise FileNotFoundError(f'Nenhum arquivo CSV encontrado em {input_dir}')

    all_data = []
    for file in csv_files:
        df = pd.read_csv(file)
        all_data.append(df)

    df_all = pd.concat(all_data, ignore_index=True)

    # Exemplo de agregação: contagem de cervejarias por estado
    df_agg = df_all.groupby('state').size().reset_index(name='brewery_count')

    output_file = os.path.join(output_dir, f'breweries_gold_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    df_agg.to_csv(output_file, index=False)

    print(f'Agregação salva em: {output_file}')

with DAG(
    dag_id='gold_aggregate_breweries',
    start_date=datetime(2025, 6, 19),
    schedule_interval=None,
    catchup=False,
    tags=['gold', 'brewery'],
) as dag:

    aggregate_task = PythonOperator(
        task_id='aggregate_breweries_data',
        python_callable=aggregate_breweries
    )
