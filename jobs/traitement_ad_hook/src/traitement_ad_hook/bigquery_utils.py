import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account


def get_bigquery_job_query_as_dataframe(query: str) -> pd.DataFrame:
    """Function Return pandas dataframe for the query in parameter"""

    client = bigquery.Client()
    return client.query(query).to_dataframe()


def get_bigquery_job_query_as_json(query: str) -> list[dict]:
    """Function Return list of dict for the query in parameter"""

    client = bigquery.Client()
    query_job = client.query(query)
    results = query_job.result()

    return [dict(row) for row in results]
