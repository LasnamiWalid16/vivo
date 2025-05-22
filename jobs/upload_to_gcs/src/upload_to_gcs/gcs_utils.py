import json
import logging
import os
import re
import time

from google.cloud import storage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def list_file_paths_in_directory(directory_path: str) -> list[str]:
    """Return a list of all files path in a given directory_path"""
    try:
        file_paths = [
            os.path.join(directory_path, f)
            for f in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, f))
        ]
        logger.info(f"{len(file_paths)} files found in '{directory_path}'")
        return file_paths
    except Exception as e:
        logger.error(
            f"Error while reading the directory {directory_path}: {e}",
            exc_info=True,
        )
        return []


"""
Upload to GCS using gcloud auth
Documentation: https://cloud.google.com/storage/docs/uploading-objects
"""


def upload_blob(bucket_name, source_file_name, destination_folder_name="raw_data"):
    """Uploads a file to GCS bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS bucket folder: optional
    # destination_folder_name = "storage-object-name"

    filename = os.path.basename(source_file_name)
    destination_blob_name = (
        f"{destination_folder_name}/{filename}" if destination_folder_name else filename
    )

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # If the file is a JSON file, clean it before uploading
    if filename.lower().endswith(".json"):
        with open(source_file_name, "r", encoding="utf-8") as f:
            file_content = f.read()
        cleaned_json_content = re.sub(r",\s*(\]|\})", r"\1", file_content)
        data_cleaned_json_content = json.loads(cleaned_json_content)
        # Convert to NDJSON
        converted_cleaned_json_content = "\n".join(
            json.dumps(item) for item in data_cleaned_json_content
        )
        blob.upload_from_string(
            converted_cleaned_json_content, content_type="application/json"
        )
    else:
        blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")
