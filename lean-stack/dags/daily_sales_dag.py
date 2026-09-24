from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="daily_sales_pipeline",
    start_date=datetime(2026, 9, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    run_sales_pipeline = BashOperator(
        task_id="run_sales_pipeline",
        bash_command="python /opt/airflow/scripts/transform_sales.py",
    )
