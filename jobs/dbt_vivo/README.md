# DBT JOB

This job Transform the raw data (external tables) to actionable models

## Prerequisites

Before running the job, make sure you have:

- BigQuery dataset for dbt transformation
- A service account key with  **bigquery.dataEditor** role

## How it works
Inside **\src\dbt_vivo\dbt_vivo_project**, the logic for modeling:
- **models\staging**: Folder containing All source data transformed
    - stg_raw_pubmed.sql: Final table for the pubmed data with union of the two pubmed sources (pubmed.csv & pubmed.json)
    - The others sources are also created as tables (clinical_trials.sql, drugs.sql)
    - yml file for each model for meta data documentation and testing
- **models\marts**: Two sql models:
    - drug_graph.sql: the json that represent the output asked (graphe de liaison entre les différents médicaments)
    - journal_most_mention_drugs.sql: contains the results of the question Traitement ad-hoc (first question)
- **macros**:
    - format_date.sql: macro named **format_date(date_column)** that transform the string date column to date type
    - string_utils.sql: macro named **clean_string(column_name)** clean the string column (if empty/null then return null)
- **packages.yml**: I've added the dbt_utils package to simplify the tests in the model's yml files doc
- **\src\dbt_vivo\main.py**: Run the dbt job 

## Setup

1. Install dependencies using **Poetry**
   ```bash
   poetry install

2. Add the service account JSON key file to the root directory of the job.

3. Create a .env file in the root of your project and insert your key/value pairs in the following format of KEY=VALUE:
    ```.env
    PROJECT_ID=gcp-project-id
    DBT_DATASET_PROD=dbt-dataset
    KEYPATH_PROD=path-to-service-account-json-key
    LOCATION_PROD=dbt-dataset-location

4. Make sure to export the env variables:
    - if you are on windows:
    ```powershell
    $env:PROJECT_ID=gcp-project-id
    $env:DBT_DATASET_PROD="vivo_dbt_dev" 
    $env:KEYPATH_PROD=path-to-service-account-json-key
    $env:LOCATION_PROD=dbt-dataset-location
    ```
    - if you are on MAC/linux:
    ```bash
    export PROJECT_ID=gcp-project-id
    export DBT_DATASET_PROD="vivo_dbt_dev" 
    export KEYPATH_PROD=path-to-service-account-json-key
    export LOCATION_PROD=dbt-dataset-location

5. **Run the dbt Job**. The main.py contains two bash commands:
    - dbt deps : to install the packages in the file packages.yml
    - dbt build : run both dbt run & dbt test
   ```bash
   poetry run python src/dbt_vivo/main.py
