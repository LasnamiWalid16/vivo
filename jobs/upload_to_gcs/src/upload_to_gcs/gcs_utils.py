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


def upload_csv_to_gcs(
    path: str, bucket_name: str, service_account_file: str, folder: str = "raw_data"
) -> None:
    """Uploads a CSV file to GCS."""
    try:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        filename = os.path.basename(path)
        blob_name = f"{folder}/{filename}" if folder else filename

        client = storage.Client.from_service_account_json(service_account_file)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(content, content_type="text/csv")
        # Wait for confirmation that the object exists
        for _ in range(10):
            if blob.exists():
                logger.info(f"Confirmed: CSV uploaded://{bucket_name}/{blob_name}")
                break
            time.sleep(1)
        else:
            logger.warning(
                f"Upload done but object not found immediately: gs://{bucket_name}/{blob_name}"
            )

    except Exception as e:
        logger.error(f"CSV upload error ({path}): {e}", exc_info=True)


def upload_json_to_gcs(
    path: str, bucket_name: str, service_account_file: str, folder: str = "raw_data"
) -> None:
    """Uploads a JSON file (converted to NDJSON) to GCS"""
    try:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            file_content = f.read()
            # Remove trailing commas before closing brackets
            cleaned_json_content = re.sub(r",\s*(\]|\})", r"\1", file_content)
            data = json.loads(cleaned_json_content)
            # Convert to NDJSON
            content = "\n".join(json.dumps(item) for item in data)

        filename = os.path.basename(path)
        blob_name = f"{folder}/{filename}" if folder else filename

        client = storage.Client.from_service_account_json(service_account_file)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(content, content_type="application/json")
        # Wait for confirmation that the object exists
        for _ in range(10):
            if blob.exists():
                logger.info(f"Confirmed: JSON uploaded://{bucket_name}/{blob_name}")
                break
            time.sleep(1)
        else:
            logger.warning(
                f"Upload done but object not found immediately: gs://{bucket_name}/{blob_name}"
            )
    except Exception as e:
        logger.error(f"JSON upload error ({path}): {e}", exc_info=True)


def upload_file_to_gcs(
    path: str, bucket_name: str, service_account_file: str, folder: str = "raw_data"
) -> None:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        upload_csv_to_gcs(path, bucket_name, service_account_file, folder)
    elif ext == ".json":
        upload_json_to_gcs(path, bucket_name, service_account_file, folder)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
