# Create external tables in BigQuery

This job creates external tables in BigQuery, referring to the files uploaded to the GCS bucket by the upload_to_gcs job.

## Prerequisites

Before running the job, make sure you have:

- BigQuery dataset
- A service account key with access to GCS **bigquery.dataEditor** role

## How it works
Inside **src/gcs_bq_external_tables**, the logic for creating external tables is as follows:
- **config.py**: Loads environment variables
- **gcs_bq_utils**: It is composed of two main functions:
    - create_external_table_from_csv: handle csv files
    - create_external_table_from_json:  handle json files
- **main.py**: Calls both functions above 

## Setup

1. Install dependencies using **Poetry**
   ```bash
   poetry install

2. Create a .env file in the root of your project and insert your key/value pairs in the following format of KEY=VALUE:
    ```.env
    BUCKET_NAME=bucket-name
    SERVICE_ACCOUNT_FILE=path-to-json-key
    PROJECT_ID=gcp-project-id
    DATASET_ID=data-set-id
    GCS_URI=files-location-uri-in-the-gcs-bucket

3. Run the Job
   ```bash
   poetry run python src/gcs_bq_external_tables/main.py
