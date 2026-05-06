# Configuration for the Jobicy remote jobs data pipeline 

from typing import List, Dict

ROLES = [
    {"role": "data_analyst", "tag": "data analyst"},
    {"role": "product_analyst", "tag": "product analyst"},
    {"role": "business_intelligence", "tag": "business intelligence"},
    {"role": "data_engineer", "tag": "data engineer"},
    {"role": "analytics_engineer", "tag": "analytics engineer"},
    {"role": "analytics", "tag": "analytics"}
]

PIPELINE_NAME = "remote_jobs_jobicy"
DATASET_NAME = "jobicy_remote_jobs_data"
BASE_URL = "https://jobicy.com/api/v2/"
PATH = "remote-jobs"
TABLE_NAME = "remote_jobs"
NUMBER_OF_JOBS = 100
DUCKDB_DESTINATION = "duckdb"
BIGQUERY_DESTINATION = "bigquery"