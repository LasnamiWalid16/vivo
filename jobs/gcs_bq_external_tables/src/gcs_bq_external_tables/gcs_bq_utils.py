import logging

from google.cloud import bigquery

# Logger config
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def create_external_table_from_csv(
    project_id: str,
    dataset_id: str,
    table_id: str,
    gcs_uri: str,
    service_account_file: str,
    autodetect: bool = True,
    schema: list = None,
) -> None:
    """
    Create an external BigQuery table from a CSV file in GCS,
    with either a defined schema or schema autodetect.
    """
    try:
        client = bigquery.Client.from_service_account_json(
            service_account_file, project=project_id
        )

        table_ref = bigquery.TableReference(
            bigquery.DatasetReference(project_id, dataset_id), table_id
        )

        client.delete_table(table_ref, not_found_ok=True)
        logger.info(f"Old table deleted: {project_id}.{dataset_id}.{table_id}")

        external_config = bigquery.ExternalConfig(bigquery.SourceFormat.CSV)
        external_config.source_uris = [gcs_uri]
        external_config.options.skip_leading_rows = 1
        external_config.autodetect = autodetect

        # Apply schema (if given)
        if schema:
            external_config.schema = [
                bigquery.SchemaField(field["name"], field["type"]) for field in schema
            ]
            external_config.autodetect = False

        table = bigquery.Table(table_ref)
        table.external_data_configuration = external_config

        table = client.create_table(table)
        logger.info(
            f"External table created: {project_id}.{dataset_id}.{table_id} - {gcs_uri}"
        )

    except Exception as e:
        logger.error(f"Error while creation external table: {e}", exc_info=True)


def create_external_table_from_json(
    project_id: str,
    dataset_id: str,
    table_id: str,
    gcs_uri: str,
    service_account_file: str,
    autodetect: bool = True,
    schema: list = None,
    json_format: str = "NEWLINE_DELIMITED_JSON",
) -> None:
    """
    Create an external BigQuery table from a json file in GCS,
    with either a defined schema or schema autodetect.
    """
    try:
        client = bigquery.Client.from_service_account_json(
            service_account_file, project=project_id
        )

        table_ref = bigquery.TableReference(
            bigquery.DatasetReference(project_id, dataset_id), table_id
        )

        client.delete_table(table_ref, not_found_ok=True)
        logger.info(f"Old table deleted: {project_id}.{dataset_id}.{table_id}")

        external_config = bigquery.ExternalConfig(
            bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
        )
        external_config.source_uris = [gcs_uri]
        external_config.autodetect = autodetect

        if schema:
            external_config.schema = [
                bigquery.SchemaField(field["name"], field["type"]) for field in schema
            ]
            external_config.autodetect = False

        table = bigquery.Table(table_ref)
        table.external_data_configuration = external_config

        client.create_table(table)
        logger.info(
            f"External table created: {project_id}.{dataset_id}.{table_id} - {gcs_uri}"
        )

    except Exception as e:
        logger.error(f"Error while creating external table: {e}", exc_info=True)
