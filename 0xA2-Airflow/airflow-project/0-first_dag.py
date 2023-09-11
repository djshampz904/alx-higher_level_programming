from airflow import DAG
from datetime import datetime

default_args = {
        "owner" : "j.doe",
        "email" : "jdoe@gmail.com",
        "start_date" : datetime(2023, 1, 1)
        }
etl_dag = DAG("etl_workflow", default_args=default_args)

