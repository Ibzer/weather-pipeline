from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/opt/airflow/ingestion')
from fetch_weather import fetch_and_insert

default_args = {
    'owner': 'ibra',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='weather_pipeline',
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule_interval='@hourly',
    catchup=False,
    tags=['weather', 'etl']
) as dag:

    ingest_task = PythonOperator(
        task_id='fetch_weather_data',
        python_callable=fetch_and_insert,
        op_kwargs={'city': 'Paris', 'lat': 48.8566, 'lon': 2.3522}
    )
