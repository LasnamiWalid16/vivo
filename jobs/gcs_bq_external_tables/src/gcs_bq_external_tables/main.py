from config import DATASET_ID, GCS_URI, PROJECT_ID, SERVICE_ACCOUNT_FILE
from gcs_bq_utils import create_external_table_from_csv, create_external_table_from_json

if __name__ == "__main__":
    # drug table schema
    schema = [{"name": "atccode", "type": "STRING"}, {"name": "drug", "type": "STRING"}]

    gcs_uri = f"{GCS_URI.rstrip('/')}/drugs.csv"

    create_external_table_from_csv(
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        table_id="drugs",
        gcs_uri=gcs_uri,
        service_account_file=SERVICE_ACCOUNT_FILE,
        schema=schema,
    )

    # pubmed table schema
    schema = [
        {"name": "id", "type": "STRING"},
        {"name": "title", "type": "STRING"},
        {"name": "date", "type": "STRING"},
        {"name": "journal", "type": "STRING"},
    ]

    gcs_uri = f"{GCS_URI.rstrip('/')}/pubmed.csv"

    create_external_table_from_csv(
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        table_id="pubmed",
        gcs_uri=gcs_uri,
        service_account_file=SERVICE_ACCOUNT_FILE,
        schema=schema,
    )

    # clinical_trials table schema
    schema = [
        {"name": "id", "type": "STRING"},
        {"name": "scientific_title", "type": "STRING"},
        {"name": "date", "type": "STRING"},
        {"name": "journal", "type": "STRING"},
    ]

    gcs_uri = f"{GCS_URI.rstrip('/')}/clinical_trials.csv"

    create_external_table_from_csv(
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        table_id="clinical_trials",
        gcs_uri=gcs_uri,
        service_account_file=SERVICE_ACCOUNT_FILE,
        schema=schema,
    )

    # pubmed.json table schema
    schema = [
        {"name": "id", "type": "STRING"},
        {"name": "title", "type": "STRING"},
        {"name": "date", "type": "STRING"},
        {"name": "journal", "type": "STRING"},
    ]

    gcs_uri = f"{GCS_URI.rstrip('/')}/pubmed.json"

    create_external_table_from_json(
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        table_id="pubmed_json",
        gcs_uri=gcs_uri,
        service_account_file=SERVICE_ACCOUNT_FILE,
        schema=schema,
    )
