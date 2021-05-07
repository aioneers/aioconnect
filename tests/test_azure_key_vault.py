import aioconnect
import os


def test_is_running_on_databricks():
    res = aioconnect.azure_key_vault._is_running_on_databricks()
    assert res == False


def test_is_running_on_devops_pipeline():
    res = aioconnect.azure_key_vault._is_running_on_devops_pipeline()
    print(res)
