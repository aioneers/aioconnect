import aioconnect
import aio_data_science_py as aio
from datetime import datetime


def test_post_login():

    password = aio.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    res = aioconnect.post_login(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    assert isinstance(res, str)
    assert len(res) > 250


def test_post_create_DOT():
    password = aio.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.post_login(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.post_create_DOT(
        token=token,
        DOT_name="TEST_DOT",
        DOT_description="TEST_DOT description",
        DOT_baseline=1234,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )

    assert res.json()["message"] == "success"


def test_update_DOT_wID_wo_timestamp():
    password = aio.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.post_login(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.update_DOT_wID(
        token=token, DOT_id="606b54d1c8153d00193838bd", actuals=987
    )

    assert res.json()["message"] == "success"


def test_update_DOT_wID_w_timestamp():
    password = aio.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.post_login(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.update_DOT_wID(
        token=token,
        DOT_id="606b54d1c8153d00193838bd",
        actuals=987,
        timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    )

    assert res.json()["message"] == "success"


def test_post_create_bulk_DOT_wDOT_type_wMETRIC_type():
    username, df_t = aioconnect.transform_qlik_string(
        arg_string="UserDirectory=AZUREQLIK; UserId=sebastian.szilvas@aioneers.com;DOT_name=1045,1058,1110,1449,3114;DOT_description=4K Ultra HD_1045,4K Ultra HD_1110,4K Ultra HD_1449,4K Ultra HD_3114,TVs_1000_1058;DOT_baseline=10846.75202,210810.99078,23874.0138,77647.14595363676,78107.53207446463"
    )

    password = aio.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    mytoken = aioconnect.post_login(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.post_create_bulk_DOT(
        token=mytoken,
        dots_df=df_t,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )

    assert res.json()["message"] == "success"


def test_post_create_bulk_DOT_woDOT_type_woMETRIC_type():
    username, df_t = aioconnect.transform_qlik_string(
        arg_string="UserDirectory=AZUREQLIK; UserId=sebastian.szilvas@aioneers.com;DOT_name=1045,1058,1110,1449,3114;DOT_description=4K Ultra HD_1045,4K Ultra HD_1110,4K Ultra HD_1449,4K Ultra HD_3114,TVs_1000_1058;DOT_baseline=10846.75202,210810.99078,23874.0138,77647.14595363676,78107.53207446463"
    )

    password = aio.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    mytoken = aioconnect.post_login(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    res = aioconnect.post_create_bulk_DOT(token=mytoken, dots_df=df_t,)

    assert res.json()["message"] == "success"
