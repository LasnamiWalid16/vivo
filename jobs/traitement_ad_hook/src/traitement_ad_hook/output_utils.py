import json
import os
from datetime import date, datetime
from pathlib import Path

from bigquery_utils import get_bigquery_job_query_as_json
from drug_graph_analysis import get_drug_journals, get_top_journals_by_unique_drugs


def default_serializer(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def save_json_query_to_output_folder(
    query: str, credentials_path: str, output_folder_name: str, output_file_name: str
) -> None:
    result_json = get_bigquery_job_query_as_json(query, credentials_path)

    # Ensure the output folder exists
    output_path = Path(output_folder_name)
    output_path.mkdir(parents=True, exist_ok=True)

    # Define file path
    file_path = output_path / output_file_name

    # Write the JSON to the file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(
            result_json, f, indent=4, ensure_ascii=False, default=default_serializer
        )

    print(f"JSON saved to: {file_path}")


def save_top_journals_to_json() -> None:
    df = get_top_journals_by_unique_drugs()
    output_dir = "output"
    output_path = os.path.join(output_dir, "top_journals.json")
    df.to_json(output_path, orient="records", indent=2)


def save_list_to_json(drug_name: str, output_folder: str, output_file: str) -> None:
    data = get_drug_journals(drug_name)

    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / output_file

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False, default=default_serializer)

    print(f"JSON file saved to: {file_path}")
