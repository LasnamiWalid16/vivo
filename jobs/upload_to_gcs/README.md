# Upload to GCS

This job uploads local CSV and JSON files to a Google Cloud Storage (GCS) bucket.  

## Prerequisites

Before running the job, make sure you have:

- A Google Cloud account.
- A GCS bucket created.
- A service account key with access to GCS (At least **Storage Object User role**)

## How it works

- **config.py**: Loads environment variables
- **gcs_utils.py**:  
  - **list_file_paths_in_directory**: Lists all files inside the `data/` folder.  
  - **upload_file_to_gcs**: Uploads each file to GCS, it is composed if two main functions:
      - upload_json_to_gcs: handle json files
      - upload_csv_to_gcs:  handle csv files
- **main.py**: Calls both functions above (list_file_paths_in_directory & upload_file_to_gcs ) to upload all files located in `data/` folder.

## Setup

1. Install dependencies using **Poetry**
   ```bash
   poetry install

2. Create a .env file in the root of your project and insert your key/value pairs in the following format of KEY=VALUE:
    ```.env
    BUCKET_NAME=your-gcs-bucket-name
    SERVICE_ACCOUNT_FILE=path/to/your/service-account-key.json

3. Tests: Two test files are defined:
   - test_gcs_utils.py : unit test file test_gcs_utils.py that tests the list_file_paths_in_directory function by creating two dummy files in a temporary directory using Python's tempfile module
   - test_config: test the env variables loading
   - Run the test:
   ```poetry run pytest

4. Run the Job
   ```bash
   python src/upload_to_gcs/main.py
