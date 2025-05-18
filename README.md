# vivo
Data pipeline to extract and merge drug mentions from scientific publications and clinical trials into a structured JSON file

## Project structure:
**Please Refer to jobs folder I've created this folder to separate the logic for each job where you will find the documentation in the README.md:**
1. **upload_to_gcs**: Upload raw data (csv/json files) to GCS bucket
2. **gcs_bq_external_tables**: Create external tables in BigQuery referring to each file
3. **dbt_vivo**: DBT Job to transform and clean data:
    - I've created a macros named **format_date** to transform date column
    - Staging Folder containing All source data transformed
    - SQL model named marts/drug_graph which is a table for the JSON output (nested columns)
    - SQL model named marts/journal_most_mention_drugs.sql
4. **traitement_ad_hook**: The folder **output** contains the results:
    - drug_graph.json
    - top_journals.json
    - ETHANOL.json (Related drugs references by the same journals and not clinical_trials)
5. **sql_test**: SQL test (Not considered a job
## How to Run the Pipeline:
- Ensure you are at the root of the vivo project (Make sure to locate to each job and install the dependencies refer to each job's doc readme.md file).
- Run the orchestration script:
  ```bash
  python run_jobs.py