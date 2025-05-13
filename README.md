# vivo
Data pipeline to extract and merge drug mentions from scientific publications and clinical trials into a structured JSON file

## Please Refer to jobs folder (good practices) I've created this folder to separate the logic for each job:
### 1) Upload raw data (csv/json files) to GCS bucket
### 2) Create external tables in BigQuery referring to each file
### 3) DBT Job to transform and clean data:
    - I've created a macros named **format_date** to transform date column
    - Staging Folder containing All source data transformed
    - SQL model named marts/drug_graph which is a table for the JSON output (nested columns)
    - SQL model named marts/journal_most_mention_drugs.sql