import os

from src.upload_to_gcs import config


def test_env_variables_are_loaded(monkeypatch):
    monkeypatch.setenv("BUCKET_NAME", "my-bucket")

    from importlib import reload

    reload(config)

    assert config.BUCKET_NAME == "my-bucket"
