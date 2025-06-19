from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import json
import os

def fetch_breweries():
    url = 'https://api.openbrewerydb.org/v1/breweries'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        output_dir = '/opt/airflow/data_lake/bronze/breweries'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f'breweries_raw_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
        with open(output_file, 'w') as f:
            json.dump(data, f)
        print(f'Dados salvos em: {output_file}')
    else:
        raise Exception(f'Erro ao buscar dados da API. Status code: {response.status_code}')

with DAG(
    dag_id='bronze_ingest_breweries',
    start_date=datetime(2025, 6, 19),
    schedule_interval=None,
    catchup=False,
    tags=['bronze', 'brewery'],
) as dag:

    ingest_task = PythonOperator(
        task_id='fetch_and_save_breweries',
        python_callable=fetch_breweries
    )
