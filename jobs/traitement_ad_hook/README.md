# Bonus ad-hook

This job export the drug_graph.json and answer the questions in bonus part   

## Prerequisites

Before running the job, make sure you have:
- A service account key with roles: **bigquery.dataViewer**

## How it works
Inside **src/traitement_ad_hook**, :
- **config.py**: Loads environment variables
- **bigquery_utils.py**: Contains two main functions to interact with bigquery:
  - **get_bigquery_job_query_as_dataframe**: Takes a SQL query as parameter and return pandas dataframe  
  - **get_bigquery_job_query_as_json**: Takes a SQL query as parameter and return list of dictionaries   
- **drug_graph_analysis.py**: Respondr to the bonus part where it contains two functions:
  - **get_top_journals_by_unique_drugs**: I used pandas to get the top journals 
  - **get_drugs_journal_pubmed**: Takes the drug name as parameter and return a list of drug names 
- **output_utils.py**: I've defined this module to keep main.py clean by simply calling the functions from drug_graph_analysis.py and exporting the results to the output folder.

- **main.py**: Calls both functions above (list_file_paths_in_directory & upload_file_to_gcs ) to upload all files located in `data/` folder.

## Setup

1. Install dependencies using **Poetry**
   ```bash
   poetry install

2. Add the service account JSON key file to the root directory of the job.

3. Create a .env file in the root of your project and insert your key/value pairs in the following format of KEY=VALUE:
    ```.bash
   PROJECT_ID=gcp-project-id
   DATASET_ID=dbt-dataset
   TABLE_ID=drug_graph
   SERVICE_ACCOUNT_FILE=path-to-service-account-json

4. Tests: Two test files are defined:
   - **test_gcs_utils.py** : unit test file test_gcs_utils.py that tests the list_file_paths_in_directory function by creating two dummy files in a temporary directory using Python's tempfile module
   - **test_config**: test the env variables loading
   - Run the tests:
   ```bash
   poetry run pytest

5. Run the Job
   ```bash
   poetry run python src/traitement_ad_hook/main.py