from config import DATASET_ID, GCS_URI, PROJECT_ID
from gcs_bq_utils import create_external_table_from_csv, create_external_table_from_json

if __name__ == "__main__":
    # Create drug table
    # Define drug table schema
    schema = [{"name": "atccode", "type": "STRING"}, {"name": "drug", "type": "STRING"}]

    # Set the source_uris to point to your data in Google Cloud
    gcs_uri = f"{GCS_URI.rstrip('/')}/drugs.csv"

    create_external_table_from_csv(
        project_id=PROJECT_ID,
        dataset_id=DATASET_ID,
        table_id="drugs",
        gcs_uri=gcs_uri,
        schema=schema,
    )

    # Create pubmed table
    # Define pubmed table schema
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
        schema=schema,
    )

    # Create clinical_trials table
    # Define clinical_trials table schema
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
        schema=schema,
    )

    # Create pubmed.json table
    # Define pubmed.json table schema
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
        schema=schema,
    )
