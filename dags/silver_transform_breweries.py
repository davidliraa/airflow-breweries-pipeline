from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os
import glob
import json

def transform_breweries():
    input_dir = '/opt/airflow/data_lake/bronze/breweries'
    output_dir = '/opt/airflow/data_lake/silver/breweries'
    os.makedirs(output_dir, exist_ok=True)

    # Pega todos os arquivos JSON na pasta bronze
    json_files = glob.glob(os.path.join(input_dir, 'breweries_raw_*.json'))
    if not json_files:
        raise FileNotFoundError(f'Nenhum arquivo JSON encontrado em {input_dir}')

    all_data = []
    for file in json_files:
        with open(file, 'r') as f:
            data = json.load(f)
            all_data.extend(data)

    # Transforma em DataFrame
    df = pd.DataFrame(all_data)

    # Lista de colunas reais do schema da API
    cols = [
        'id', 'name', 'brewery_type', 'address_1', 'address_2', 'address_3',
        'city', 'state_province', 'postal_code', 'country', 'longitude',
        'latitude', 'phone', 'website_url', 'state', 'street'
    ]

    # Mantém apenas as colunas que existem no DataFrame (evita erro caso alguma venha faltando)
    df = df[[col for col in cols if col in df.columns]]

    # Remove linhas onde o nome da cervejaria está vazio
    df = df[df['name'].notna()]

    # Salva o resultado em parquet particionado por 'state'
    df.to_parquet(
        output_dir,
        partition_cols=['state'] if 'state' in df.columns else None,
        index=False,
        engine='pyarrow',  # ou 'fastparquet' se preferir
        compression='snappy'
    )

    print(f'Dados transformados salvos em parquet particionado em: {output_dir}')

with DAG(
    dag_id='silver_transform_breweries',
    start_date=datetime(2025, 6, 19),
    schedule_interval=None,
    catchup=False,
    tags=['silver', 'brewery'],
) as dag:

    transform_task = PythonOperator(
        task_id='transform_breweries_data',
        python_callable=transform_breweries
    )
