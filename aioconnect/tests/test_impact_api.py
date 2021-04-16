import json
import aioconnect
import aiox
import requests


from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential


def test_create_or_update_DOT_wName_wDescription_DOT_not_existing():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )
    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    DOT_name = "Pytest DOT"
    DOT_description = "Pytest DOT description"
    DOT_baseline = 9023
    DOT_type_id = "6019fa2072b96c00133df326"
    METRIC_type_id = "5fb7bf2f8ce87f0012fcc8f3"

    res = aioconnect.create_or_update_DOT_wName_wDescription(
        token=token,
        DOT_name=DOT_name,
        DOT_description=DOT_description,
        DOT_baseline=DOT_baseline,
        DOT_type_id=DOT_type_id,
        METRIC_type_id=METRIC_type_id,
    )

    assert res.json()["message"] == "success"

    # Clean up after creation
    aioconnect.delete_DOT_wID(
        token=token, DOT_id=res.json()["data"]["_id"],
    )


def test_create_or_update_DOT_wName_wDescription_DOT_existing():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )
    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    DOT_name = "Pytest DOT"
    DOT_description = "Pytest DOT description"
    DOT_baseline = 9023
    DOT_type_id = "6019fa2072b96c00133df326"
    METRIC_type_id = "5fb7bf2f8ce87f0012fcc8f3"

    # First create a DOT
    just_created_DOT = aioconnect.create_DOT(
        token=token,
        DOT_name=DOT_name,
        DOT_description=DOT_description,
        DOT_baseline=DOT_baseline,
        DOT_type_id=DOT_type_id,
        METRIC_type_id=METRIC_type_id,
    ).json()["data"]

    res = aioconnect.create_or_update_DOT_wName_wDescription(
        token=token,
        DOT_name=DOT_name,
        DOT_description=DOT_description,
        DOT_baseline=DOT_baseline,
        DOT_type_id=DOT_type_id,
        METRIC_type_id=METRIC_type_id,
    )

    assert res.json()["message"] == "success"

    # Clean up after creation
    aioconnect.delete_DOT_wID(
        token=token, DOT_id=just_created_DOT["_id"],
    )


def test_create_or_update_DOT_wName_wDescription_multipleDOTs():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    DOT_name = "My real TEST_DOT"
    DOT_description = "My real TEST_DOT description"
    DOT_baseline = 9503
    DOT_type_id = "6019fa2072b96c00133df326"
    METRIC_type_id = "5fb7bf2f8ce87f0012fcc8f3"

    # First create a DOT
    first_dot = aioconnect.create_DOT(
        token=token,
        DOT_name=DOT_name,
        DOT_description=DOT_description,
        DOT_baseline=DOT_baseline,
        DOT_type_id=DOT_type_id,
        METRIC_type_id=METRIC_type_id,
    ).json()["data"]

    second_dot = aioconnect.create_DOT(
        token=token,
        DOT_name=DOT_name,
        DOT_description=DOT_description,
        DOT_baseline=DOT_baseline,
        DOT_type_id=DOT_type_id,
        METRIC_type_id=METRIC_type_id,
    ).json()["data"]

    res = aioconnect.create_or_update_DOT_wName_wDescription(
        token=token,
        DOT_name=DOT_name,
        DOT_description=DOT_description,
        DOT_baseline=DOT_baseline,
        DOT_type_id=DOT_type_id,
        METRIC_type_id=METRIC_type_id,
    )

    # Clean up after creation
    aioconnect.delete_DOT_wID(token=token, DOT_id=first_dot["_id"])
    aioconnect.delete_DOT_wID(token=token, DOT_id=second_dot["_id"])

    assert res.json()["message"] == "success"


def test_get_initiative_templates():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect._get_initiative_templates(token=token,)

    print(res)

    assert isinstance(res, list)


def test_get_token():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    res = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    assert isinstance(res, str)
    assert len(res) > 250


def test_get_token_w_wrong_password():
    try:
        res = aioconnect.get_token(
            email="sebastian.szilvas@aioneers.com", password="wrong password",
        )
    except requests.exceptions.HTTPError as exception:
        print(exception)
        assert exception.response.status_code == 401


def test_delete_DOT_wID():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    # First create a DOT
    tmp_res = aioconnect.create_DOT(
        token=token,
        DOT_name="TEST_DOT",
        DOT_description="TEST_DOT description",
        DOT_baseline=1234,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )

    just_created_DOT_ID = tmp_res.json()["data"]["_id"]

    res = aioconnect.delete_DOT_wID(token=token, DOT_id=just_created_DOT_ID,)

    assert res.json()["message"] == "success"


def test_create_DOT():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.create_DOT(
        token=token,
        DOT_name="TEST_DOT",
        DOT_description="TEST_DOT description",
        DOT_baseline=1234,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )

    assert res.json()["message"] == "success"

    # Clean up after creation
    just_created_DOT_ID = res.json()["data"]["_id"]
    aioconnect.delete_DOT_wID(
        token=token, DOT_id=just_created_DOT_ID,
    )


def test_create_DOT_wo_DOT_description():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.create_DOT(
        token=token,
        DOT_name="TEST_DOT",
        DOT_baseline=1234,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )

    assert res.json()["message"] == "success"

    # Clean up after creation
    just_created_DOT_ID = res.json()["data"]["_id"]
    aioconnect.delete_DOT_wID(
        token=token, DOT_id=just_created_DOT_ID,
    )


def test_update_DOT_wID_wo_timestamp():
    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    # First create a DOT
    tmp_res = aioconnect.create_DOT(
        token=token,
        DOT_name="TEST_DOT",
        DOT_description="TEST_DOT description",
        DOT_baseline=1234,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )
    just_created_DOT_ID = tmp_res.json()["data"]["_id"]

    res = aioconnect.update_DOT_wID(
        token=token, DOT_id=just_created_DOT_ID, actuals=987
    )

    assert res.json()["message"] == "success"


def test_update_DOT_wID_w_timestamp():
    from datetime import datetime

    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    # First create a DOT
    tmp_res = aioconnect.create_DOT(
        token=token,
        DOT_name="TEST_DOT",
        DOT_description="TEST_DOT description",
        DOT_baseline=1234,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )
    just_created_DOT_ID = tmp_res.json()["data"]["_id"]

    res = aioconnect.update_DOT_wID(
        token=token,
        DOT_id=just_created_DOT_ID,
        actuals=987,
        timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    )

    assert res.json()["message"] == "success"


def test_create_bulk_DOT_wDOT_type_wMETRIC_type():
    username, df_t = aioconnect.transform_qlik_string(
        arg_string="UserDirectory=AZUREQLIK; UserId=sebastian.szilvas@aioneers.com;DOT_name=1045,1058,1110,1449,3114;DOT_description=4K Ultra HD_1045,4K Ultra HD_1110,4K Ultra HD_1449,4K Ultra HD_3114,TVs_1000_1058;DOT_baseline=10846.75202,210810.99078,23874.0138,77647.14595363676,78107.53207446463"
    )

    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    mytoken = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.create_bulk_DOT(
        token=mytoken,
        dots_df=df_t,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )

    assert res.json()["message"] == "success"


def test_create_bulk_DOT_woDOT_type_woMETRIC_type():
    username, df_t = aioconnect.transform_qlik_string(
        arg_string="UserDirectory=AZUREQLIK; UserId=sebastian.szilvas@aioneers.com;DOT_name=1045,1058,1110,1449,3114;DOT_description=4K Ultra HD_1045,4K Ultra HD_1110,4K Ultra HD_1449,4K Ultra HD_3114,TVs_1000_1058;DOT_baseline=10846.75202,210810.99078,23874.0138,77647.14595363676,78107.53207446463"
    )

    password = aiox.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    mytoken = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.create_bulk_DOT(token=mytoken, dots_df=df_t,)

    assert res.json()["message"] == "success"
