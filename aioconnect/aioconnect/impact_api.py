import requests
from requests import Request, Session
import io
import pandas as pd
from datetime import datetime
import json
import aioconnect


def get_metric_type_id_wMetricName(token: str, metric_name: str):
    """
    Create a new DOT in AIO Impact or update it if the DOT is already existing.

    Parameters
    ----------
    token : str
        Token which was returned from the user login.

    metric_name : str
        Name of the metric type. Current options are "Financial", "Percentage", "Countable", "Other", "My second DOT"

    Returns
    -------

    _id : str
        ID of the metric type.


    """
    url = "https://dev-api.aioneers.tech/v1/metrictypes"

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        url=url,
        headers=headers,
    )

    response_json = response.json()["data"]["payload"]

    all_metric_names = aioconnect.json_extract(response_json, "name")

    index_of_metric = all_metric_names.index(metric_name)

    _id = response.json()["data"]["payload"][index_of_metric]["_id"]

    return _id


def create_or_update_DOT_wName_wDescription(
    token: str,
    DOT_name: str,
    DOT_baseline: float,
    DOT_description: str = None,
    DOT_type_id: str = "6019fa2072b96c00133df326",
    METRIC_type_id: str = "5fb7bf2f8ce87f0012fcc8f3",
):
    """
    Create a new DOT in AIO Impact or update it if the DOT is already existing.

    Parameters
    ----------
    token : str
        Token which was returned from the user login.

    DOT_name : str
        Name of the DOT.

    DOT_baseline : float
        Baseline value of the DOT.

    DOT_description : str = DOT_name
        Description of the DOT.

    DOT_type_id : str = "6019fa2072b96c00133df326"
        ID of the DOT type.

    METRIC_type_id : str = "5fb7bf2f8ce87f0012fcc8f3"
        ID of the METRIC type.

    Returns
    -------

    response : response
        HTTP response.

    Examples
    --------
    >>> token = aioconnect.get_token(
    >>> email="firstname.lastname@aioneers.com", password="xxx",
    >>> )
    >>>
    >>> res = aioconnect.create_or_update_DOT_wName_wDescription(
    >>>     token=token,
    >>>     DOT_name="TEST_DOT",
    >>>     DOT_description="TEST_DOT description",
    >>>     DOT_baseline=1234,
    >>>     DOT_type_id="6019fa2072b96c00133df326",
    >>>     METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    >>> )
    """

    url = "https://dev-api.aioneers.tech/v1/trackingObjects"
    url = url.rstrip("/")
    url += "?name=" + DOT_name

    if DOT_description == None:
        DOT_description = DOT_name
    else:
        url += "&description=" + DOT_description

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        url=url,
        headers=headers,
    )
    response.raise_for_status()

    total = response.json()["data"]["total"]
    # print("total: ", total)

    if total == 0:
        res = create_DOT(
            token=token,
            DOT_name=DOT_name,
            DOT_baseline=DOT_baseline,
            DOT_description=DOT_description,
            DOT_type_id=DOT_type_id,
            METRIC_type_id=METRIC_type_id,
        )
    elif total == 1:
        DOT_id = response.json()["data"]["payload"][0]["_id"]
        res = update_DOT_wID(
            token=token, DOT_id=DOT_id, actuals=DOT_baseline, timestamp=None
        )
    else:
        # Update every DOT with that DOT_name
        for i in range(total):
            DOT_id = response.json()["data"]["payload"][i]["_id"]
            res = update_DOT_wID(
                token=token, DOT_id=DOT_id, actuals=DOT_baseline, timestamp=None
            )

    return res


def _get_initiative_templates(token: str):
    """
    Get the initiative templates

    Parameters
    ----------
    token : str
        Token which was returned from the user login.

    Returns
    -------

    res : list
        Initiative templates as list.

    Examples
    --------
    >>> token = aioconnect.get_token(
    >>> email="firstname.lastname@aioneers.com", password="xxx",
    >>> )
    >>> res = aioconnect._get_initiative_templates(
    >>>     token = token,
    >>> )
    """

    url = "https://dev-api.aioneers.tech/v1/initiativeTemplates"
    url = url.rstrip("/")

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        url=url,
        headers=headers,
    )
    response.raise_for_status()

    res = response.json()["data"]["payload"]

    return res


def get_token(
    email: str,
    password: str,
):
    """
    Log into AIO Impact and get a token.

    Parameters
    ----------
    email : str
        Email address of the user account.

    password : str
        Password of the user account.

    Returns
    -------

    token : str
        Bearer token.

    Examples
    --------
    >>> aioconnect.get_token(
    >>>     email="firstname.lastname@aioneers.com", password="xxx",
    >>> )
    """

    url = "https://dev-api.aioneers.tech/v1/login"
    url = url.rstrip("/")

    payload = {"email": email, "password": password}

    response = requests.post(url=url, data=payload)
    response.raise_for_status()

    token = response.json()["data"]["token"]

    return token


def delete_DOT_wID(token: str, DOT_id: str):
    """
    Function to delete a DOT.

    Parameters
    ----------
    token : str
        Token which was returned from the user login.

    DOT_id : str
        ID of the DOT.

    Returns
    -------

    response : response
        Returns the HTTP response.

    Examples
    --------
    >>> token = aioconnect.get_token(
    >>> email="firstname.lastname@aioneers.com", password="xxx",
    >>> )
    >>> res = delete_DOT_wID(
    >>>     token = token,
    >>>     DOT_id = "606b54d1c8153d00193838bd",
    >>> )
    """

    url = "https://dev-api.aioneers.tech/v1/trackingObjects/"
    url = url.rstrip("/")
    url += "/" + DOT_id

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url=url, headers=headers)
    response.raise_for_status()

    return response


def update_DOT_wID(token: str, DOT_id: str, actuals: float, timestamp: str = None):
    """
    Function to update a DOT and add the most recent actual value.

    Parameters
    ----------
    token : str
        Token which was returned from the user login.

    DOT_id : str
        ID of the DOT.

    actuals : float
        Most recent actuals value.

    timestamp : str = None
        Timestamp of the actual data in the format .

    Returns
    -------

    response : response
        Returns the HTTP response.

    Examples
    --------
    >>> from datetime import datetime
    >>>
    >>> token = aioconnect.get_token(
    >>> email="firstname.lastname@aioneers.com", password="xxx",
    >>> )
    >>> res = update_DOT_wID(
    >>>     token = token,
    >>>     DOT_id = "606b54d1c8153d00193838bd",
    >>>     actuals = 889,
    >>>     timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    >>> )
    """

    if timestamp is None:
        datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")

    url = "https://dev-api.aioneers.tech/v1/trackingObjects"
    url = url.rstrip("/")

    # Get actuals history
    headers = {"Authorization": f"Bearer {token}"}
    params = {"_id": {DOT_id}}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    actuals_history = response.json()["data"]["payload"][0]["actuals"]

    # Append actuals history with new value
    new_actuals = {"timestamp": timestamp, "value": actuals}
    actuals_history.append(new_actuals)

    data = {
        "_id": DOT_id,
        "actuals": actuals_history,
    }

    response = requests.put(url=url, json=data, headers=headers)
    return response


def create_DOT(
    token: str,
    DOT_name: str,
    DOT_baseline: float,
    DOT_description: str = None,
    DOT_type_id: str = "6019fa2072b96c00133df326",
    METRIC_type_id: str = "5fb7bf2f8ce87f0012fcc8f3",
):
    """
    Create a new DOT in AIO Impact.

    Parameters
    ----------
    DOT_name : str
        Name of the DOT.

    DOT_baseline : float
        Baseline value of the DOT.

    DOT_description : str = DOT_name
        Description of the DOT.

    DOT_type_id : str = "6019fa2072b96c00133df326"
        ID of the DOT type.

    METRIC_type_id : str = "5fb7bf2f8ce87f0012fcc8f3"
        ID of the METRIC type.

    Returns
    -------

    response : response
        HTTP response.

    Examples
    --------
    >>> token = aioconnect.get_token(
    >>> email="firstname.lastname@aioneers.com", password="xxx",
    >>> )
    >>>
    >>> res = aioconnect.create_DOT(
    >>>     token=token,
    >>>     DOT_name="TEST_DOT",
    >>>     DOT_description="TEST_DOT description",
    >>>     DOT_baseline=1234,
    >>>     DOT_type_id="6019fa2072b96c00133df326",
    >>>     METRIC_type_id="5fb7bf2f8ce87f0012fcc8f3",
    >>> )
    """

    if DOT_description == None:
        DOT_description = DOT_name

    url = "https://dev-api.aioneers.tech/v1/trackingObjects"
    url = url.rstrip("/")

    payload = json.dumps(
        {
            "name": DOT_name,
            "description": DOT_description,
            "type": DOT_type_id,
            "baseline": DOT_baseline,
            "metricType": {"_id": METRIC_type_id},
        }
    )
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    response = requests.post(url=url, headers=headers, data=payload)
    response.raise_for_status()

    return response


def create_bulk_DOT(
    token: str,
    dots_df: pd.DataFrame,
    DOT_type_id: str = "6019fa2072b96c00133df326",
    METRIC_type_id: str = "5fb7bf2f8ce87f0012fcc8f3",
):
    """
    Function to create DOTs from a data frame and additional information.

    Parameters
    ----------
    token : str
        Token which was returned from the user login.

    dots_df : Pandas.DataFrame
        Dataframe which contains the information in the same format as it would be in the CSV upload.

    DOT_type_id : str
        ID of the DOT type.

    METRIC_type_id : str
        ID of the METRIC type.

    Returns
    -------

    response : response
        Returns the HTTP response.

    Examples
    --------
    >>> username, df_t = transform_qlik_string(arg_string = "UserDirectory=AZUREQLIK; UserId=sebastian.szilvas@aioneers.com;DOT_name=1045,1058,1110,1449,3114;DOT_description=4K Ultra HD_1045,4K Ultra HD_1110,4K Ultra HD_1449,4K Ultra HD_3114,TVs_1000_1058;DOT_baseline=10846.75202,210810.99078,23874.0138,77647.14595363676,78107.53207446463")
    >>> mytoken = get_token()
    >>> res = create_bulk_DOT(
    >>>     token = mytoken,
    >>>     dots_df = df_t,
    >>>     DOT_type_id = "6019fa2072b96c00133df326",
    >>>     METRIC_type_id = "5fb7bf2f8ce87f0012fcc8f3",
    >>> )
    """

    dots_df = dots_df.rename(
        columns={
            "DOT_name": "Tracking_Object_Name",
            "DOT_description": "Tracking_Object_Description",
            "DOT_baseline": "Tracking_Object_Baseline",
        }
    )

    url = "https://dev-api.aioneers.tech/v1/trackingObjects/upload"
    url = url.rstrip("/")

    headers = {"Authorization": f"Bearer {token}"}

    with io.StringIO(dots_df.to_csv(index=False)) as openstream:
        request = Request(
            method="POST",
            url=url,
            files={
                "trackingObjectTypeId": (None, DOT_type_id),
                "metricTypeId": (None, METRIC_type_id),
                "file": ("file", openstream, "text/csv"),
            },
            headers=headers,
        ).prepare()

    s = Session()
    response = s.send(request)
    response.raise_for_status()

    return response


# To be deprecated
def transform_qlik_string(arg_string: str):
    """
    Transform the string input from Qlik Sense and extract the relevant information.

    Parameters
    ----------
    arg_string : str
        Input string sent from Qlik Sense.

    Returns
    -------

    username : str
        The username, extracted from the string.

    df_t : Pandas.DataFrame
        A dataframe containing the information in a structured format.

    Examples
    --------
    >>> input_from_qlik = "UserDirectory=AZUREQLIK; UserId=sebastian.szilvas@aioneers.com;DOT_name=1045,1058,1110,1449,3114;DOT_description=4K Ultra HD_1045,4K Ultra HD_1110,4K Ultra HD_1449,4K Ultra HD_3114,TVs_1000_1058;DOT_baseline=10846.75202,210810.99078,23874.0138,77647.14595363676,78107.53207446463"
    >>> (username, dots_df) = transform_qlik_string(arg_string=input_from_qlik)
    """

    df = pd.DataFrame(data=arg_string.split(";"))

    df = df[0].str.split(
        pat="=",
        expand=True,
    )
    df.columns = ["Field", "Value"]

    username = df[df["Field"] == " UserId"].Value
    df = df[df["Field"] != " UserId"]  # Delete the user name
    df = df[df["Field"] != "UserDirectory"]  # Delete the user directory

    cols_count = df["Value"].str.split(",", expand=True).shape[1]
    for c in range(cols_count):
        df["Value" + str(c + 1)] = df["Value"].str.split(",", expand=True)[c]

    df_t = df.T
    df_t.columns = df_t.iloc[0]
    df_t = df_t.iloc[2:]
    return (username, df_t)
