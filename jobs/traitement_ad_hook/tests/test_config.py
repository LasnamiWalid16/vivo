import os

from src.traitement_ad_hook import config


def test_env_variables_are_loaded(monkeypatch):
    monkeypatch.setenv("DBT_DATASET", "dbt-dataset")

    from importlib import reload

    reload(config)

    assert config.DBT_DATASET == "dbt-dataset"
