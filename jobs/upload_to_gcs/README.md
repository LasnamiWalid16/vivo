# Upload to GCS

This job uploads local CSV and JSON files to a Google Cloud Storage (GCS) bucket.  

## Prerequisites

Before running the job, make sure you have:

- A Google Cloud account.
- A GCS bucket created.
- A service account key with access to GCS with roles: storage.objectCreator and storage.objectViewer

## How it works

- **config.py**: Loads environment variables like bucket name and service account path.
- **gcs_utils.py**:  
  - **list_file_paths_in_directory**: Lists all files inside the `data/` folder.  
  - **upload_file_to_gcs**: Uploads each file to GCS.
- **main.py**: Calls both functions above to upload all files in the `data/` folder.

## Setup

1. Install dependencies using **Poetry**
   ```bash
   poetry install

2. Create a .env file in the root folder with the following content:
```.env
BUCKET_NAME=your-gcs-bucket-name
SERVICE_ACCOUNT_FILE=path/to/your/service-account-key.json

3. Run the Job
   ```bash
   python src/upload_to_gcs/main.py
