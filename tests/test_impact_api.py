import json
import aioconnect
from aioconnect.helpers import get_values
import requests
from requests.exceptions import InvalidURL
import pandas as pd

from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential
from requests.models import guess_json_utf


class Test_get_object:
    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )
    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
    )

    # def test_dot(self):
    #     assert aioconnect.get_object(
    #         token=self.token,
    #         object="dottypes",
    #     )

    # def test_DOT(self):
    #     assert aioconnect.get_object(
    #         token=self.token,
    #         object="DOTtypes",
    #     )

    # def test_measures(self):
    #     assert aioconnect.get_object(
    #         token=self.token,
    #         object="measures",
    #     )

    # def test_initiatives(self):
    #     print("the correct URL is:")
    #     print(CONNECT_URL1)
    #     assert aioconnect.get_object(
    #         token=self.token,
    #         object="initiatives",
    #     )

    def test_digitalObjectTwins(self):
        assert aioconnect.get_object(
            token=self.token,
            object="digitalObjectTwins",
        )

    def test_measures(self):
        assert aioconnect.get_object(
            token=self.token,
            object="measures",
        )

    def test_initiatives(self):
        assert aioconnect.get_object(
            token=self.token,
            object="initiatives",
        )

    def test_hdjfhskhkfd(self):
        try:
            assert aioconnect.get_object(
                token=self.token,
                object="hdjfhskhkfd",
            )
        except KeyError:
            pass


class Test_get_list:
    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )
    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
    )

    def test_hdjfhskhkfd(self):
        try:
            assert aioconnect.get_list(
                token=self.token,
                key="name",
                object="hdjfhskhkfd",
            )
        except KeyError:
            pass


class Test_get_token:
    def test_correct_credentials(self):
        password = aioconnect.vault_get_secret(
            scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
        )

        res = aioconnect.get_token(
            email="sebastian.szilvas@aioneers.com",
            password=f"{password}",
        )

        assert isinstance(res, str)
        assert len(res) > 250

    def test_wrong_password(self):
        try:
            res = aioconnect.get_token(
                email="sebastian.szilvas@aioneers.com",
                password="wrong password",
            )
        except KeyError as exception:
            print(exception)
            # assert exception.response.status_code == 401


# def test_delete_DOT_wID():
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )

#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com",
#         password=f"{password}",
#     )

#     # First create a DOT
#     tmp_res = aioconnect.create_DOT(
#         token=token,
#         DOT_name="TEST_DOT",
#         DOT_description="TEST_DOT description",
#         DOT_baseline=1234,
#         DOT_type_id="6019fa2072b96c00133df326",
#         METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
#     )

#     just_created_DOT_ID = tmp_res.json()["data"]["_id"]

#     res = aioconnect.delete_DOT_wID(
#         token=token,
#         DOT_id=just_created_DOT_ID,
#     )

# assert res.json()["message"] == "success"


# def test_create_DOT():
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )

#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com",
#         password=f"{password}",
#     )

#     res = aioconnect.create_DOT(
#         token=token,
#         DOT_name="TEST_DOT",
#         DOT_description="TEST_DOT description",
#         DOT_baseline=1234,
#         DOT_type_id="6019fa2072b96c00133df326",
#         METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
#     )

# assert res.json()["message"] == "success"

# # Clean up after creation
# just_created_DOT_ID = res.json()["data"]["_id"]
# aioconnect.delete_DOT_wID(
#     token=token,
#     DOT_id=just_created_DOT_ID,
# )


class Test_upsert_DOT:
    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
    )

    # def test_single_DOT_correct_headers(self):

    #     from datetime import datetime

    #     columns = [
    #         "DOT_name",
    #         "DOT_description",
    #         "DOT_type",
    #         "DOT_value",
    #         "DOT_date_time",
    #     ]

    #     dict = {
    #         "DOT_name": "1000",
    #         "DOT_description": "Basic Desktop_1000",
    #         "DOT_Type": "Standard",
    #         "DOT_Value": 2.7771,
    #         "DOT_date_time": "03-05-2021  09:57:00",
    #     }
    #     df = pd.DataFrame(data=dict)

    #     assert aioconnect.upsert_DOT(token=self.token, dataframe=df).status_code == 200

    def test_single_DOT_incorrect_headers(self):
        columns_list = [
            "DOT_description",
            "DOT_type",
            "DOT_value",
            "DOT_date_time",
        ]

        df = pd.DataFrame(columns=columns_list)

        df.loc[0] = [
            "Basic Desktop_1000",
            "Standard",
            2.7771,
            "03-05-2021 09:57:00",
        ]
        try:
            assert (
                aioconnect.upsert_DOT(token=self.token, dataframe=df).status_code == 200
            )
        except ValueError as exc:
            print(exc)
