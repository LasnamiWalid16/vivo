import os

from bigquery_utils import load_bigquery_query_as_dataframe, load_bigquery_query_as_json
from config import PROJECT_ID, SERVICE_ACCOUNT_FILE
from drug_graph_analysis import get_drug_journals, get_top_journals_by_unique_drugs

table_id = "drug_graph"
dataset_id = "vivo_dbt_dev"

full_table_id = f"{PROJECT_ID}.{dataset_id}.{table_id}"
query = f"SELECT * FROM `{full_table_id}`"


def save_top_journals_to_json():
    df = get_top_journals_by_unique_drugs()

    output_dir = "output"
    output_path = os.path.join(output_dir, "top_journals.json")
    df.to_json(output_path, orient="records", indent=2)


if __name__ == "__main__":
    # save_top_journals_to_json()
    # print(load_bigquery_query_as_json(query,SERVICE_ACCOUNT_FILE))
    print(get_drug_journals("ETHANOL"))
