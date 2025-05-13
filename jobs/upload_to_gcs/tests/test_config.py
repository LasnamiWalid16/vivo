import os

from src.upload_to_gcs import config


def test_env_variables_are_loaded(monkeypatch):
    monkeypatch.setenv("BUCKET_NAME", "my-bucket")
    monkeypatch.setenv("SERVICE_ACCOUNT_FILE", "credentials.json")

    # Reimport config to refresh loaded variables
    from importlib import reload

    reload(config)

    assert config.BUCKET_NAME == "my-bucket"
    assert config.SERVICE_ACCOUNT_FILE == "credentials.json"
