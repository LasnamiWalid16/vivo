# Upload to GCS

This job uploads local CSV and JSON files to a Google Cloud Storage bucket.  

## Prerequisites

Before running the job, make sure you have:

- A Google Cloud account.
- A GCS bucket created.
- The Google Cloud SDK (gcloud CLI) installed and initialized.
- You are authenticated using the following command:
   ```bash
   gcloud auth application-default login

## How it works
Inside **src/upload_to_gcs**, the logic for uploading files is as follows:
- **config.py**: Loads environment variables
- **gcs_utils.py** contains two main functions:  
  - **list_file_paths_in_directory**: Lists all files inside the `data/` folder.  
  - **upload_blob**: Uploads each file to GCS. [Google Cloud documentation](https://cloud.google.com/storage/docs/uploading-objects):
- **main.py**: Calls both functions above (list_file_paths_in_directory & upload_blob ) to upload all files located in `data/` folder.

## Setup

1. Install dependencies using **Poetry**
   ```bash
   poetry install

2. Create a .env file in the root of your project and insert your key/value pairs in the following format of KEY=VALUE:
    ```.env
    BUCKET_NAME=your-gcs-bucket-name

4. Tests: Two test files are defined:
   - **test_gcs_utils.py** : unit test file test_gcs_utils.py that tests the list_file_paths_in_directory function by creating two dummy files in a temporary directory using python's tempfile module
   - **test_config**: test the env variables loading
   - Run the tests:
   ```bash
   poetry run pytest

5. Run the Job
   ```bash
   poetry run python src/upload_to_gcs/main.py