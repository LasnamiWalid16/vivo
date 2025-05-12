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




def convert_json_to_ndjson(json_path: str) -> str:
    """
    Convertit un fichier JSON contenant une liste d'objets en fichier NDJSON.
    Retourne le chemin du fichier NDJSON.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Format du fichier JSON incorrect ({json_path}): {e}")

    if not isinstance(data, list):
        raise ValueError(f"Le contenu JSON doit être une liste d'objets: {json_path}")

    ndjson_path = json_path.replace(".json", ".ndjson")
    with open(ndjson_path, "w", encoding="utf-8") as f:
        for item in data:
            if isinstance(item, dict):
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
            else:
                raise ValueError("Chaque élément du tableau JSON doit être un objet (dict).")

    return ndjson_path



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
