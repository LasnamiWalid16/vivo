from gcs_to_bq_external import create_external_table_from__csv, create_external_table_from_json
from google.cloud import bigquery
from urllib.parse import urljoin

from config import DATASET_ID, PROJECT_ID, GCS_URI,SERVICE_ACCOUNT_FILE

if __name__ == '__main__':
   
    #Reference drugs table
    schema = [
    {"name": "atccode", "type": "STRING"},
    {"name": "drug", "type": "STRING"}
    ]

    gcs_uri = f"{GCS_URI.rstrip('/')}/drugs.csv"

    create_external_table_from__csv(
    project_id=PROJECT_ID,
    dataset_id=DATASET_ID,
    table_id="drugs",
    gcs_uri=gcs_uri,
    service_account_file=SERVICE_ACCOUNT_FILE,
    schema=schema
    )

    #Reference pubmed table
    schema = [
    {"name": "id", "type": "STRING"},
    {"name": "title", "type": "STRING"},
    {"name": "date", "type": "STRING"},
    {"name": "journal", "type": "STRING"}
    ]

    gcs_uri = f"{GCS_URI.rstrip('/')}/pubmed.csv"

    create_external_table_from__csv(
    project_id=PROJECT_ID,
    dataset_id=DATASET_ID,
    table_id="pubmed",
    gcs_uri=gcs_uri,
    service_account_file=SERVICE_ACCOUNT_FILE,
    schema=schema
    )
    
    #Reference clinical_trials table
    schema = [
    {"name": "id", "type": "STRING"},
    {"name": "scientific_title", "type": "STRING"},
    {"name": "date", "type": "STRING"},
    {"name": "journal", "type": "STRING"}
    ]

    gcs_uri = f"{GCS_URI.rstrip('/')}/clinical_trials.csv"

    create_external_table_from__csv(
    project_id=PROJECT_ID,
    dataset_id=DATASET_ID,
    table_id="clinical_trials",
    gcs_uri=gcs_uri,
    service_account_file=SERVICE_ACCOUNT_FILE,
    schema=schema
    )
    
    
    #Reference pubmed.json table
    schema = [
    {"name": "id", "type": "STRING"},
    {"name": "title", "type": "STRING"},
    {"name": "date", "type": "STRING"},
    {"name": "journal", "type": "STRING"}
    ]

    gcs_uri = f"{GCS_URI.rstrip('/')}/pubmed.json"

    create_external_table_from_json(
    project_id=PROJECT_ID,
    dataset_id=DATASET_ID,
    table_id="pubmed_json",
    gcs_uri=gcs_uri,
    service_account_file=SERVICE_ACCOUNT_FILE,
    schema=schema
    )