from google.cloud import bigquery 
from google.oauth2 import service_account
import pandas as pd



def load_bigquery_query_as_dataframe(query:str, credentials_path:str) -> pd.DataFrame:
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = bigquery.Client(credentials=credentials)
    return client.query(query).to_dataframe()


def load_bigquery_query_as_json(query: str, credentials_path: str) -> list[dict]:
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = bigquery.Client(credentials=credentials)

    query_job = client.query(query)
    results = query_job.result()

    return [dict(row) for row in results]