
from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Import OCI 
import oci

# Operators; we need this to operate!
from airflow.operators.bash import PythonOperator
with DAG(
    "oci_start_instance",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "owner": "hfolguera",
        "email": ["hfolguera@gmail.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple start OCI instance example",
    schedule=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example", "oci", "oracle"],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = PythonOperator(
        task_id="start_instance",
        python_callable=test_function,
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )
    t1.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
    **Image Credit:** Randall Munroe, [XKCD](https://xkcd.com/license.html)
    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG; OR
    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this

    t1 >> t2













# from datetime import datetime
# from airflow import DAG
# import oci
# from airflow.operators.bash import PythonOperator

# default_args = {'owner': 'hfolguera',
#                 'start_date': datetime(2023, 1, 1),
#                 'email': ['hfolguera@gmail.com'],
#                 'email_on_failure': False,
#                 'email_on_retry': False
#                 }

# dag = DAG('oci_start_instance',
#           default_args=default_args,
#           schedule_interval='@daily',
#           catchup=False
#           )

# oci_conn_id = "oci_default"
# #bucketname = "SomeBucketName"
# compartment_ocid = "ocid1.tenancy.oc1..aaaaaaaa3roehpairwhfhzenxbmofim6ies4h7cvcowbzv26ia3oiq47ygga"

# with dag:
#     make_bucket = MakeBucket(task_id='Make_Bucket', bucket_name=bucketname,oci_conn_id=oci_conn_id, compartment_ocid=compartment_ocid)

    