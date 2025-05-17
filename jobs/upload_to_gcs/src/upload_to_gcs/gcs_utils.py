import json
import logging
import os
import re

from config import MOCK_MODE
from google.cloud import storage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def list_file_paths_in_directory(directory_path: str) -> list[str]:
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


def upload_file_to_gcs(
    path: str, bucket_name: str, service_account_file: str, folder: str = "raw_data"
) -> None:
    """
    Upload CSV/JSON to GCS bucket (folder by default = raw_data)
    If the file extension is json it will convert it to NDJSON.
    """
    if (
        MOCK_MODE == True
    ):  # If not GCP envirement than dont execute the block for uploading
        logger.info(
            f"[MOCK_MODE] Simulated upload for file {path} to bucket {bucket_name}"
        )
        return
    try:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Fichier introuvable: {path}")

        ext = os.path.splitext(path)[1].lower()

        if ext == ".csv":
            content_type = "text/csv"
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            filename = os.path.basename(path)

        elif ext == ".json":
            with open(path, "r", encoding="utf-8") as f:
                first_char = f.read(1)
                f.seek(0)
                content = f.read()
                # Remove last ",]" if exists
                content = re.sub(r",\s*\]", "]", content)  # Nettoyage simple

                if first_char == "[":  # tableau JSON → NDJSON
                    data = json.load(f)
                    if not isinstance(data, list):
                        raise ValueError(
                            "Le fichier JSON doit contenir un array à la racine."
                        )
                    # Convertit en NDJSON (en mémoire, sans fichier intermédiaire)
                    content = "\n".join(json.dumps(item) for item in data)
                else:
                    content = f.read()  # JSON object classique

            content_type = "application/json"
            filename = os.path.basename(path).replace(
                ".json", ".json"
            )  # garder le même nom

        else:
            raise ValueError(f"Extension de fichier non supportée: {ext}")

        # Construire le chemin du blob
        blob_name = f"{folder}/{filename}" if folder else filename

        # Upload
        client = storage.Client.from_service_account_json(service_account_file)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(content, content_type=content_type)

        logger.info(f"Fichier uploadé avec succès: gs://{bucket_name}/{blob_name}")

    except Exception as e:
        logger.error(
            f"Erreur lors de l'upload du fichier {path} vers GCS: {e}", exc_info=True
        )
