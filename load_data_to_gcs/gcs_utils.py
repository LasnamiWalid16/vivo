from google.cloud import storage
import json
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def list_file_paths_in_directory(directory_path: str) -> list[str]:

    try:
        file_paths = [
            os.path.join(directory_path, f)
            for f in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, f))
        ]
        logger.info(f"{len(file_paths)} fichier(s) trouvé(s) dans le répertoire '{directory_path}'")
        return file_paths
    except Exception as e:
        logger.error(f"Erreur lors de la lecture du répertoire {directory_path}: {e}", exc_info=True)
        return []


def upload_file_to_gcs(path: str, bucket_name: str, service_account_file: str, folder: str = "data") -> None:
    """
    Upload un fichier CSV ou JSON dans un bucket GCS, dans le dossier spécifié.
    Si c'est un JSON contenant une liste (array), il est converti à la volée en NDJSON.
    """
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
                if first_char == "[":  # tableau JSON → NDJSON
                    data = json.load(f)
                    if not isinstance(data, list):
                        raise ValueError("Le fichier JSON doit contenir un array à la racine.")
                    # Convertit en NDJSON (en mémoire, sans fichier intermédiaire)
                    content = "\n".join(json.dumps(item) for item in data)
                else:
                    content = f.read()  # JSON objet classique

            content_type = "application/json"
            filename = os.path.basename(path).replace(".json", ".json")  # garder le même nom

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
        logger.error(f"Erreur lors de l'upload du fichier vers GCS: {e}", exc_info=True)
