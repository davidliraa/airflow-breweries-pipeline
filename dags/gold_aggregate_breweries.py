from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os

def aggregate_breweries():
    input_dir = '/opt/airflow/data_lake/silver/breweries'  # diretório raiz do parquet particionado
    output_dir = '/opt/airflow/data_lake/gold/breweries'
    os.makedirs(output_dir, exist_ok=True)

    # Lê o parquet particionado apontando para o diretório
    try:
        df_all = pd.read_parquet(input_dir, engine='pyarrow')  # ou fastparquet
    except Exception as e:
        raise FileNotFoundError(f'Erro ao ler parquet particionado em {input_dir}: {e}')

    # Agregação por brewery_type e estado (state ou state_province)
    # Ajuste aqui conforme coluna existente no df
    state_col = 'state' if 'state' in df_all.columns else 'state_province'

    df_agg = (
        df_all.groupby([state_col, 'brewery_type'])
        .size()
        .reset_index(name='brewery_count')
        .sort_values(by=[state_col, 'brewery_type'])
    )

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
