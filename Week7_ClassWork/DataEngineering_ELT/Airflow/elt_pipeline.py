from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import requests
import sqlalchemy

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

with DAG("elt_pipeline", schedule_interval="@daily", default_args=default_args) as dag:

    def extract():
        try:
            url = "https://api.publicapis.org/entries"
            response = requests.get(url)
            data = response.json()["entries"]
        except:
            # fallback: use local file
            import json
            with open('/opt/airflow/dags/sample_entries.json', 'r') as f:
                data = json.load(f)["people"]

        df = pd.DataFrame(data)
        df.to_csv("/tmp/raw_data.csv", index=False)

    def transform():
        df = pd.read_csv("/tmp/raw_data.csv")
        df["full_name"] = df["firstName"] + " " + df["lastName"]
        df.to_csv("/tmp/cleaned_data.csv", index=False)


    def load():
        df = pd.read_csv("/tmp/cleaned_data.csv")
        if df.isnull().any().any():
            raise ValueError("Null values found in data")
        engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:root@host.docker.internal:3306/sales")
        df.to_sql("public_apis", engine, if_exists="replace", index=False)

    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)

    t1 >> t2 >> t3
