
import pytest
import aioconnect
from aioconnect.helpers import get_values
import requests

import pandas as pd


from requests.models import guess_json_utf
from datetime import datetime


# # This needs fixing
# class Test_get_object:
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )
#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com",
#         password=f"{password}",
#     )

#     def test_digitalObjectTwins(self):
#         assert aioconnect.get_object(
#             token=self.token,
#             object="digitalObjectTwins",
#         )

#     def test_measures(self):
#         assert aioconnect.get_object(
#             token=self.token,
#             object="measures",
#         )

#     def test_initiatives(self):
#         assert aioconnect.get_object(
#             token=self.token,
#             object="initiatives",
#         )

#     def test_hdjfhskhkfd(self):
#         try:
#             assert aioconnect.get_object(
#                 token=self.token,
#                 object="hdjfhskhkfd",
#             )
#         except KeyError:
#             pass


# class Test_get_list:
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )
#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com",
#         password=f"{password}",
#     )

#     def test_hdjfhskhkfd(self):
#         try:
#             assert aioconnect.get_list(
#                 token=self.token,
#                 key="name",
#                 object="hdjfhskhkfd",
#             )
#         except KeyError:
#             pass


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
        except requests.exceptions.HTTPError as exception:
            assert exception.response.status_code == 401


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


# class Test_upsert_DOT:
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )

#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com",
#         password=f"{password}",
#     )

#     def test_single_DOT_correct_headers(self):
#         data = {
#             "externalID": ["8493", ],
#             "name": ["4K Ultra HD_1008", ],
#             "metricType": ["Financial", ],
#             "actuals": [[
#                 {
#                         "timestamp": "Mon, 02 Mar 2020 00:00:00 GMT",
#                         "value": 2398
#                         }
#             ],
#             ]
#         }
#         df = pd.DataFrame.from_dict(data)

#         res = aioconnect.upsert_DOT(
#             token=self.token, dataframe=df)

#         assert res.status_code == 200
#         assert (res.json()["created"] == len(df.index) or
#                 res.json()["updated"] == len(df.index))
#         assert res.json()["failed"] == 0

#     def test_two_DOTs_correct_headers(self):
#         data = {
#             "externalID": ["8493", "7843"],
#             "name": ["4K Ultra HD_1008", "sdfjlsdf"],
#             "metricType": ["Financial", "Financial"],
#             "actuals": [[
#                 {
#                         "timestamp": "Mon, 02 Mar 2020 00:00:00 GMT",
#                         "value": 2398
#                         }
#             ], [
#                 {
#                     "timestamp": "Mon, 02 Mar 2020 00:00:00 GMT",
#                     "value": 50000
#                 }
#             ]
#             ]
#         }
#         df = pd.DataFrame.from_dict(data)

#         res = aioconnect.upsert_DOT(
#             token=self.token, dataframe=df)

#         assert res.status_code == 200
#         assert (res.json()["created"] == len(df.index) or
#                 res.json()["updated"] == len(df.index))
#         assert res.json()["failed"] == 0

#     def test_single_DOT_incorrect_headers(self):
#         data = {
#             "jksljfls": ["8493", ],
#             "dkflusdf": ["4K Ultra HD_1008", ],
#             "dfjksdf": ["Financial", ],
#             "dfd": [[
#                 {
#                     "timestamp": "Mon, 02 Mar 2020 00:00:00 GMT",
#                     "value": 2398
#                 }
#             ],
#             ]
#         }
#         df = pd.DataFrame.from_dict(data)

#         try:
#             aioconnect.upsert_DOT(
#                 token=self.token, dataframe=df)

#         except KeyError as exc:
#             assert "Columns not correct" in str(exc)

#     @pytest.mark.skip(reason="takes too long")
#     def test_single_DOT_correct_headers_negative_values(self):
#         data = {
#             "externalID": ["8493", ],
#             "name": ["4K Ultra HD_1008", ],
#             "metricType": ["Financial", ],
#             "actuals": [[
#                 {
#                         "timestamp": "Mon, 02 Mar 2020 00:00:00 GMT",
#                         "value": -2398
#                         }
#             ],
#             ]
#         }
#         df = pd.DataFrame.from_dict(data)

#         res = aioconnect.upsert_DOT(
#             token=self.token, dataframe=df)

#         assert res.status_code == 200
#         assert res.json()["created"] == 0
#         assert res.json()["updated"] == 0
#         assert res.json()["failed"] == len(df.index)
