import pandas as pd
from bigquery_utils import (
    get_bigquery_job_query_as_dataframe,
    get_bigquery_job_query_as_json,
)
from config import PROJECT_ID, SERVICE_ACCOUNT_FILE


def get_top_journals_by_unique_drugs() -> pd.DataFrame:
    # Define variables
    table_id = "drug_graph"
    dataset_id = "vivo_dbt_dev"
    full_table_id = f"{PROJECT_ID}.{dataset_id}.{table_id}"
    query = f"SELECT * FROM `{full_table_id}`"

    # Get the drug_graph dataframe
    df = get_bigquery_job_query_as_dataframe(query, SERVICE_ACCOUNT_FILE)

    # Explod mentions column
    df_exploded = df.explode("mentions")

    # extract journal et atccode
    df_exploded["journal"] = df_exploded["mentions"].apply(
        lambda x: x.get("journal") if isinstance(x, dict) else None
    )
    df_clean = df_exploded[["journal", "atccode"]].dropna()

    # drop duplicates
    df_unique = df_clean.drop_duplicates()

    # count number of drugs per journal
    journal_counts = (
        df_unique.groupby("journal")["atccode"]
        .nunique()
        .reset_index(name="unique_drugs_count")
    )

    # find max
    max_count = journal_counts["unique_drugs_count"].max()

    # Return les journaux ayant le max
    top_journals = journal_counts[journal_counts["unique_drugs_count"] == max_count]

    return top_journals


def get_drug_journals(drug: str) -> list[str]:
    # Get the json drug_graph from bigquery
    table_id = "drug_graph"
    dataset_id = "vivo_dbt_dev"
    full_table_id = f"{PROJECT_ID}.{dataset_id}.{table_id}"
    query = f"SELECT * FROM `{full_table_id}`"
    data = get_bigquery_job_query_as_json(query, SERVICE_ACCOUNT_FILE)

    # Extract unique journals where the drug is mentioned in pubmed only
    journals = {
        mention["journal"].strip()
        for row in data
        for mention in row.get("mentions", [])
        if mention.get("source") == "pubmed"
        and drug.lower() in mention.get("title", "").lower()
    }

    journals_list = list(journals)

    reference_journal_drugs_pubmed = {
        row["drug"]
        for row in data
        for mention in row.get("mentions", [])
        if mention.get("source") == "pubmed"
        and mention.get("journal", "") in journals_list
    }

    reference_journal_drugs_clinical = {
        row["drug"]
        for row in data
        for mention in row.get("mentions", [])
        if mention.get("source") == "clinical_trial"
        and mention.get("journal", "") in journals_list
    }

    # remove drugs mentioned in cliniv=cal trials
    result = list(
        set(list(reference_journal_drugs_pubmed))
        - set(list(reference_journal_drugs_clinical))
    )
    # remove the drug in parameter from the output LISt
    if drug in result:
        result.remove(drug)

    return result
