from config import DBT_DATASET, PROJECT_ID
from output_utils import (
    list_to_json,
    save_json_query_to_output_folder,
    save_top_journals_to_json,
)

# Define the query to get the drug_graph table from bigquery
table_id = "drug_graph"
full_table_id = f"{PROJECT_ID}.{DBT_DATASET}.{table_id}"
query_drug_graph = f"SELECT * FROM `{full_table_id}`"


if __name__ == "__main__":
    # Export drug_graph.json to output/drug_graph.json ()
    save_json_query_to_output_folder(
        query=query_drug_graph,
        output_folder_name="output",
        output_file_name="drug_graph.json",
    )

    # Export top_journals as json to output/top_journals.json
    save_top_journals_to_json()

    # Export the related list of drugs as json to output/drug_name.json
    list_to_json(
        drug_name="ETHANOL", output_folder="output", output_file="ETHANOL.json"
    )
