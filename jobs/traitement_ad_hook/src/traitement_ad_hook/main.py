from config import PROJECT_ID, SERVICE_ACCOUNT_FILE
from drug_graph_analysis import get_drug_journals
from output_utils import (
    save_json_query_to_output_folder,
    save_list_to_json,
    save_top_journals_to_json,
)

table_id = "drug_graph"
dataset_id = "vivo_dbt_dev"
full_table_id = f"{PROJECT_ID}.{dataset_id}.{table_id}"
query_drug_graph = f"SELECT * FROM `{full_table_id}`"


if __name__ == "__main__":
    save_json_query_to_output_folder(
        query_drug_graph, SERVICE_ACCOUNT_FILE, "output", "drug_graph.json"
    )
    save_top_journals_to_json()
    save_list_to_json("ETHANOL", output_folder="output", output_file="ETHANOL.json")
