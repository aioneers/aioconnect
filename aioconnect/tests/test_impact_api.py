import aioconnect
import aio_data_science_py as aio


def test_post_login():

    password = aio.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    res = aioconnect.post_login(
        email="sebastian.szilvas@aioneers.com", password=f"{password}",
    )

    assert isinstance(res, str)
    assert len(res) > 250
