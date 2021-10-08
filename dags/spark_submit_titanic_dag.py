from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago

with DAG(
    'spark_submit_titanic_k8s',
    default_args={
        'owner': 'jmuniz',
        'depends_on_past': False,
        'max_active_runs': 1,
    },
    description='submit spark as sparkApplication on kubernetes',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=['spark', 'kubernetes', 'batch'],
) as dag:
    titanic_process = SparkKubernetesOperator(
        task_id='titanic_process',
        namespace="airflow-spark-ns",
        application_file="yamls/titanic_process.yaml",
        kubernetes_conn_id="kubernetes_default",
        do_xcom_push=True,
    )
    titanic_sensor = SparkKubernetesSensor(
        task_id='titanic_sensor',
        namespace="airflow-spark-ns",
        application_name="{{ task_instance.xcom_pull(task_ids='titanic_process')['metadata']['name'] }}",
        kubernetes_conn_id="kubernetes_default",
    )

titanic_process >> titanic_sensor