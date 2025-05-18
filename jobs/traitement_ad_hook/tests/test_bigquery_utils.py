from unittest.mock import MagicMock, patch

from src.traitement_ad_hook.bigquery_utils import get_bigquery_job_query_as_json


@patch(
    "google.cloud.bigquery.Client"
)  # mock the Client class from google.cloud.bigquery
@patch("google.oauth2.service_account.Credentials")  # mock credentials
def test_get_bigquery_job_query_as_json(mock_credentials, mock_bigquery_client):
    # Setup mock return value for result
    mock_row_1 = {"drug": "drug1", "code": 123}
    mock_row_2 = {"drug": "drug2", "code": 658}
    mock_result = [mock_row_1, mock_row_2]

    mock_query_job = MagicMock()
    mock_query_job.result.return_value = [mock_row_1, mock_row_2]

    mock_client_instance = MagicMock()
    mock_client_instance.query.return_value = mock_query_job

    mock_bigquery_client.return_value = mock_client_instance

    result = get_bigquery_job_query_as_json(
        "SELECT drug, code FROM table", "fake_path.json"
    )

    assert result == mock_result
    mock_bigquery_client.assert_called_once()
    mock_client_instance.query.assert_called_once_with("SELECT drug, code FROM table")
