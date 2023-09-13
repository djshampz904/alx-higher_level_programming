from airflow.models import DAG
from airflow.python_operators import PythonOperator

default_args = {
        "owner" : "g.doe",
        "email" : "gdoe@gmail.com",
        "start_date" : datetime(2023, 1, 1)
        }

py_dag = DAG('python_operatio', default_args=default_args)

def printme():
    print("Hello there")

py_task = PythonOperator(
        task_id="print_python",
        python_callable=printme,
        dag=py_dag
        )
