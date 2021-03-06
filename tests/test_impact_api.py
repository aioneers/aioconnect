import json
import aioconnect
from aioconnect.helpers import get_values
import requests
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

    def test_dot(self):
        assert aioconnect.get_object(
            token=self.token,
            object="dottypes",
        )

    def test_DOT(self):
        assert aioconnect.get_object(
            token=self.token,
            object="DOTtypes",
        )

    def test_METRIC(self):
        assert aioconnect.get_object(
            token=self.token,
            url="https://dev-api.aioneers.tech/v1/",
            object="METRICtypes",
        )

    def test_metricTypes(self):
        assert aioconnect.get_object(
            token=self.token,
            object="metricTypes",
        )

    def test_metrics(self):
        assert aioconnect.get_object(
            token=self.token,
            object="metrics",
        )

    def test_dots(self):
        assert aioconnect.get_object(
            token=self.token,
            object="dots",
        )

    def test_trackingObjectTypes(self):
        assert aioconnect.get_object(
            token=self.token,
            object="trackingObjectTypes",
        )

    def test_actions(self):
        assert aioconnect.get_object(
            token=self.token,
            object="actions",
        )

    def test_actionTemplates(self):
        assert aioconnect.get_object(
            token=self.token,
            object="actionTemplates",
        )

    def test_measureTemplates(self):
        assert aioconnect.get_object(
            token=self.token,
            object="measureTemplates",
        )

    def test_measures(self):
        assert aioconnect.get_object(
            token=self.token,
            object="measures",
        )

    def test_initiativeTemplates(self):
        assert aioconnect.get_object(
            token=self.token,
            object="initiativeTemplates",
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
        except ValueError:
            pass


class Test_get_list:
    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )
    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
    )

    def test_dot(self):
        assert aioconnect.get_list(
            token=self.token,
            key="name",
            object="dottypes",
        ) == [
            "Material",
            "Master Data Object",
            "Master Data Process",
            "Asset",
            "Line",
            "Production Department",
            "Customer Invoice",
            "Supplier Invoice",
            "Supplier",
            "Customer",
            "Process",
            "Plant",
            "IT System",
            "Supplier Segment",
            "Cost Center",
            "Warehouse",
            "Lane",
            "Destination",
            "Project",
            "Product Group",
            "Product Segment",
            "Customer Segment",
            "Standard",
            "Data Object",
            "Capacity Resource",
            "Business Partner",
            "Organizational Unit",
            "Account",
            "Location",
            "Relation",
            "Document Type",
        ]

    def test_DOT(self):
        assert aioconnect.get_list(
            token=self.token,
            key="name",
            object="DOTtypes",
        ) == [
            "Material",
            "Master Data Object",
            "Master Data Process",
            "Asset",
            "Line",
            "Production Department",
            "Customer Invoice",
            "Supplier Invoice",
            "Supplier",
            "Customer",
            "Process",
            "Plant",
            "IT System",
            "Supplier Segment",
            "Cost Center",
            "Warehouse",
            "Lane",
            "Destination",
            "Project",
            "Product Group",
            "Product Segment",
            "Customer Segment",
            "Standard",
            "Data Object",
            "Capacity Resource",
            "Business Partner",
            "Organizational Unit",
            "Account",
            "Location",
            "Relation",
            "Document Type",
        ]

    def test_METRIC(self):
        assert (
            aioconnect.get_list(
                token=self.token,
                url="https://dev-api.aioneers.tech/v1/",
                key="name",
                object="METRICtypes",
            )
            == ["Financial", "Percentage", "Countable", "Other", "My second DOT"]
        )

    def test_metric(self):
        assert aioconnect.get_list(
            token=self.token,
            key="name",
            object="metrictypes",
        ) == [
            "Financial",
            "Percentage",
            "Countable",
            "Other",
            "My second DOT",
        ]

    def test_metric_IDs(self):
        assert aioconnect.get_list(
            token=self.token,
            key="_id",
            object="metrictypes",
        ) == [
            "5fb7bf2f8ce87f0012fcc8f3",
            "5fb7cc5c8ce87f0012fcc918",
            "60018ae0f10fa9001326747c",
            "6019ed8072b96c00133df30d",
            "6063127e01b2550013be8b63",
        ]

    def test_metric_IDs_no_key(self):
        assert aioconnect.get_list(token=self.token, object="metrictypes",) == [
            "5fb7bf2f8ce87f0012fcc8f3",
            "5fb7cc5c8ce87f0012fcc918",
            "60018ae0f10fa9001326747c",
            "6019ed8072b96c00133df30d",
            "6063127e01b2550013be8b63",
        ]

    def test_hdjfhskhkfd(self):
        try:
            assert aioconnect.get_list(
                token=self.token,
                key="name",
                object="hdjfhskhkfd",
            )
        except ValueError:
            pass


# def test_get_DOT_type_id_wDOT_type_Name():

#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )
#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com", password=f"{password}",
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Material")
#         == "5fb7bf528ce87f0012fcc8f4"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Master Data Object"
#         )
#         == "5fb7bf598ce87f0012fcc8f5"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Master Data Process"
#         )
#         == "5fb7bf628ce87f0012fcc8f6"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Asset")
#         == "5fb7bf678ce87f0012fcc8f7"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Line")
#         == "5fb7bf6a8ce87f0012fcc8f8"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Production Department"
#         )
#         == "5fb7bf7b8ce87f0012fcc8f9"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Customer Invoice"
#         )
#         == "5fb7bf828ce87f0012fcc8fa"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Supplier Invoice"
#         )
#         == "5fb7bf888ce87f0012fcc8fb"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Supplier")
#         == "5fb7bf8c8ce87f0012fcc8fc"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Customer")
#         == "5fb7bf8f8ce87f0012fcc8fd"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Process")
#         == "5fb7bf958ce87f0012fcc8fe"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Plant")
#         == "5fb7bf9a8ce87f0012fcc8ff"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="IT System"
#         )
#         == "5fb7bf9e8ce87f0012fcc900"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Supplier Segment"
#         )
#         == "600fcaed52b0c500125fec82"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Cost Center"
#         )
#         == "600fcaf952b0c500125fec87"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Warehouse"
#         )
#         == "600fcafa52b0c500125fec88"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Lane")
#         == "600fcafc52b0c500125fec89"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Destination"
#         )
#         == "600fcafd52b0c500125fec8a"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Destination"
#         )
#         == "600fcafd52b0c500125fec8a"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Project")
#         == "600fcaff52b0c500125fec8b"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Product Group"
#         )
#         == "600fcb2452b0c500125fec8d"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Product Segment"
#         )
#         == "600fcb2452b0c500125fec8e"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Customer Segment"
#         )
#         == "600fcb2552b0c500125fec8f"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Standard")
#         == "6019fa2072b96c00133df326"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Data Object"
#         )
#         == "6019fa7b72b96c00133df327"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Capacity Resource"
#         )
#         == "6019fa9672b96c00133df328"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Business Partner"
#         )
#         == "6019fb2672b96c00133df329"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Organizational Unit"
#         )
#         == "6019fb4572b96c00133df32a"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Account")
#         == "6019fb7172b96c00133df32b"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Location")
#         == "6019fb8f72b96c00133df32c"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(token=token, DOT_type_name="Relation")
#         == "6019fbaa72b96c00133df32d"
#     )

#     assert (
#         aioconnect.get_DOT_type_id_wDOT_type_name(
#             token=token, DOT_type_name="Document Type"
#         )
#         == "6019fbbf72b96c00133df32e"
#     )


# def test_get_metric_type_id_wMetric_type_name():

#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )
#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com", password=f"{password}",
#     )

#     assert (
#         aioconnect.get_metric_type_id_wMetric_type_name(
#             token=token, metric_type_name="Financial"
#         )
#         == "5fb7bf2f8ce87f0012fcc8f3"
#     )

#     assert (
#         aioconnect.get_metric_type_id_wMetric_type_name(
#             token=token, metric_type_name="Percentage"
#         )
#         == "5fb7cc5c8ce87f0012fcc918"
#     )

#     assert (
#         aioconnect.get_metric_type_id_wMetric_type_name(
#             token=token, metric_type_name="Countable"
#         )
#         == "60018ae0f10fa9001326747c"
#     )

#     assert (
#         aioconnect.get_metric_type_id_wMetric_type_name(
#             token=token, metric_type_name="Other"
#         )
#         == "6019ed8072b96c00133df30d"
#     )

#     assert (
#         aioconnect.get_metric_type_id_wMetric_type_name(
#             token=token, metric_type_name="My second DOT"
#         )
#         == "6063127e01b2550013be8b63"
#     )


# def test_create_or_update_DOT_wName_wDescription_DOT_not_existing():
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )
#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com", password=f"{password}",
#     )

#     DOT_name = "Pytest DOT"
#     DOT_description = "Pytest DOT description"
#     DOT_baseline = 9023
#     DOT_type_id = "6019fa2072b96c00133df326"
#     METRIC_type_id = "5fb7bf2f8ce87f0012fcc8f3"

#     res = aioconnect.create_or_update_DOT_wName_wDescription(
#         token=token,
#         DOT_name=DOT_name,
#         DOT_description=DOT_description,
#         DOT_baseline=DOT_baseline,
#         DOT_type_id=DOT_type_id,
#         METRIC_type_id=METRIC_type_id,
#     )

#     assert res.json()["message"] == "success"

#     # Clean up after creation
#     aioconnect.delete_DOT_wID(
#         token=token, DOT_id=res.json()["data"]["_id"],
#     )


# def test_create_or_update_DOT_wName_wDescription_DOT_existing():
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )
#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com", password=f"{password}",
#     )

#     DOT_name = "Pytest DOT"
#     DOT_description = "Pytest DOT description"
#     DOT_baseline = 9023
#     DOT_type_id = "6019fa2072b96c00133df326"
#     METRIC_type_id = "5fb7bf2f8ce87f0012fcc8f3"

#     # First create a DOT
#     just_created_DOT = aioconnect.create_DOT(
#         token=token,
#         DOT_name=DOT_name,
#         DOT_description=DOT_description,
#         DOT_baseline=DOT_baseline,
#         DOT_type_id=DOT_type_id,
#         METRIC_type_id=METRIC_type_id,
#     ).json()["data"]

#     res = aioconnect.create_or_update_DOT_wName_wDescription(
#         token=token,
#         DOT_name=DOT_name,
#         DOT_description=DOT_description,
#         DOT_baseline=DOT_baseline,
#         DOT_type_id=DOT_type_id,
#         METRIC_type_id=METRIC_type_id,
#     )

#     assert res.json()["message"] == "success"

#     # Clean up after creation
#     aioconnect.delete_DOT_wID(
#         token=token, DOT_id=just_created_DOT["_id"],
#     )


# def test_create_or_update_DOT_wName_wDescription_multipleDOTs():
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )

#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com", password=f"{password}",
#     )

#     DOT_name = "My real TEST_DOT"
#     DOT_description = "My real TEST_DOT description"
#     DOT_baseline = 9503
#     DOT_type_id = "6019fa2072b96c00133df326"
#     METRIC_type_id = "5fb7bf2f8ce87f0012fcc8f3"

#     # First create a DOT
#     first_dot = aioconnect.create_DOT(
#         token=token,
#         DOT_name=DOT_name,
#         DOT_description=DOT_description,
#         DOT_baseline=DOT_baseline,
#         DOT_type_id=DOT_type_id,
#         METRIC_type_id=METRIC_type_id,
#     ).json()["data"]

#     second_dot = aioconnect.create_DOT(
#         token=token,
#         DOT_name=DOT_name,
#         DOT_description=DOT_description,
#         DOT_baseline=DOT_baseline,
#         DOT_type_id=DOT_type_id,
#         METRIC_type_id=METRIC_type_id,
#     ).json()["data"]

#     res = aioconnect.create_or_update_DOT_wName_wDescription(
#         token=token,
#         DOT_name=DOT_name,
#         DOT_description=DOT_description,
#         DOT_baseline=DOT_baseline,
#         DOT_type_id=DOT_type_id,
#         METRIC_type_id=METRIC_type_id,
#     )

#     # Clean up after creation
#     aioconnect.delete_DOT_wID(token=token, DOT_id=first_dot["_id"])
#     aioconnect.delete_DOT_wID(token=token, DOT_id=second_dot["_id"])

#     assert res.json()["message"] == "success"


# def test_get_initiative_templates():
#     password = aioconnect.vault_get_secret(
#         scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
#     )

#     token = aioconnect.get_token(
#         email="sebastian.szilvas@aioneers.com", password=f"{password}",
#     )

#     res = aioconnect._get_initiative_templates(token=token,)

#     print(res)

#     assert isinstance(res, list)


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
            print(exception)
            assert exception.response.status_code == 401


def test_delete_DOT_wID():
    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
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

    res = aioconnect.delete_DOT_wID(
        token=token,
        DOT_id=just_created_DOT_ID,
    )

    assert res.json()["message"] == "success"


def test_create_DOT():
    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
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
        token=token,
        DOT_id=just_created_DOT_ID,
    )


def test_create_DOT_wo_DOT_description():
    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    token = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
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
        token=token,
        DOT_id=just_created_DOT_ID,
    )


# def test_update_DOT_wID_wo_timestamp():
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

#     res = aioconnect.update_DOT_wID(
#         token=token, DOT_id=just_created_DOT_ID, actuals=987
#     )

#     assert res.json()["message"] == "success"


# def test_update_DOT_wID_w_timestamp():
#     from datetime import datetime

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

#     res = aioconnect.update_DOT_wID(
#         token=token,
#         DOT_id=just_created_DOT_ID,
#         actuals=987,
#         timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
#     )

#     assert res.json()["message"] == "success"


def test_create_bulk_DOT_wDOT_type_wMETRIC_type():
    username, df_t = aioconnect.transform_string(
        arg_string="UserDirectory=AZUREQLIK; UserId=sebastian.szilvas@aioneers.com;DOT_name=1045,1058,1110,1449,3114;DOT_description=4K Ultra HD_1045,4K Ultra HD_1110,4K Ultra HD_1449,4K Ultra HD_3114,TVs_1000_1058;DOT_baseline=10846.75202,210810.99078,23874.0138,77647.14595363676,78107.53207446463"
    )

    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    mytoken = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
    )

    res = aioconnect.create_bulk_DOT(
        token=mytoken,
        dots_df=df_t,
        DOT_type_id="6019fa2072b96c00133df326",
        METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    )

    assert res.json()["message"] == "success"


def test_create_bulk_DOT_woDOT_type_woMETRIC_type():
    username, df_t = aioconnect.transform_string(
        arg_string="UserDirectory=AZUREQLIK; UserId=sebastian.szilvas@aioneers.com;DOT_name=1045,1058,1110,1449,3114;DOT_description=4K Ultra HD_1045,4K Ultra HD_1110,4K Ultra HD_1449,4K Ultra HD_3114,TVs_1000_1058;DOT_baseline=10846.75202,210810.99078,23874.0138,77647.14595363676,78107.53207446463"
    )

    password = aioconnect.vault_get_secret(
        scope="aio-data-science-key", key="sebastian-szilvas-aio-impact"
    )

    mytoken = aioconnect.get_token(
        email="sebastian.szilvas@aioneers.com",
        password=f"{password}",
    )

    res = aioconnect.create_bulk_DOT(
        token=mytoken,
        dots_df=df_t,
    )

    assert res.json()["message"] == "success"


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
                aioconnect.upsert_DOT(
                    token=self.token, dataframe=df).status_code == 200
            )
        except ValueError as exc:
            print(exc)
