from gcs_utils import list_file_paths_in_directory,upload_file_to_gcs
from config import BUCKET_NAME, SERVICE_ACCOUNT_FILE


if __name__ == '__main__':       
    file_paths = list_file_paths_in_directory("data")
    for file_path in file_paths:
        upload_file_to_gcs(file_path, BUCKET_NAME, SERVICE_ACCOUNT_FILE)
