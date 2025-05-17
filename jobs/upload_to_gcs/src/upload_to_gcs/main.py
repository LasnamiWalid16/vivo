from config import BUCKET_NAME, SERVICE_ACCOUNT_FILE
from gcs_utils import list_file_paths_in_directory, upload_file_to_gcs

# The code bellow calls the function list_file_paths_in_directory to get the the list of all file_paths located in data folder
# For each file path, call the 'upload_file_to_gcs' function from gcs_utils.py
# This function handles the upload of CSV or JSON files to the specified GCS bucket

if __name__ == "__main__":
    file_paths = list_file_paths_in_directory(
        "data"
    )  # Get all files (list) paths located in the folder'data'
    for file_path in file_paths:
        upload_file_to_gcs(
            file_path, BUCKET_NAME, SERVICE_ACCOUNT_FILE, folder="data"
        )  # Upload each file in file_paths list
