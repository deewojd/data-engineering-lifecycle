from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="daily_sales_spark_pipeline",
    start_date=datetime(2026, 9, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    run_spark_pipeline = BashOperator(
        task_id="run_spark_pipeline",
        bash_command=(
            "/opt/spark/bin/spark-submit "
            "--master spark://spark-master:7077 "
            "--deploy-mode client "
            "--conf spark.driver.host=spark-airflow "
            "--conf spark.driver.bindAddress=0.0.0.0 "
            "/opt/airflow/scripts/transform_sales.py"
        ),
    )
