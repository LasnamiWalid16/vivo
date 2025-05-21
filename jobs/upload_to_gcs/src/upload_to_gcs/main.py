from config import BUCKET_NAME
from gcs_utils import list_file_paths_in_directory, upload_blob

# The code bellow calls the function list_file_paths_in_directory to get the the list of all file_paths located in data folder
# For each file path, call the 'upload_file_to_gcs' function from gcs_utils.py
# This function handles the upload of CSV or JSON files to the specified GCS bucket
# make sure to run the command: gcloud auth application-default login

if __name__ == "__main__":
    # Get all files (list) paths located in the folder'data'
    file_paths = list_file_paths_in_directory("data")

    # Upload each file in file_paths list
    for file_path in file_paths:
        upload_blob(
            bucket_name=BUCKET_NAME,
            source_file_name=file_path,
            destination_folder_name="raw_data",
        )
