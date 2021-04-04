import requests

# TODO rewrite with forms-data
def post_login(
    email: str, password: str,
):
    """
    Log into AIO Impact and get a token.

    Parameters
    ----------
    email : string
        Email address of the user account.
    
    password : string
        Password of the user account.

    Returns
    -------

    token : string
        Bearer token.

    Examples
    --------
    >>> aioconnect.post_login(
    >>>     email="firstname.lastname@aioneers.com", password="xxx",
    >>> )
    """

    url = "https://dev-api.aioneers.tech/v1/login"
    data = {"email": f"{email}", "password": f"{password}"}
    response = requests.post(url, json=data)
    token = response.json()["data"]["token"]
    return token


# TODO: rewrite with forms-datametricType, DOT_type is needed
def post_create_DOT(
    token: str,
    DOT_name: str,
    DOT_description: str,
    DOT_baseline: float,
    DOT_type: str = "6019fa2072b96c00133df326",
):
    url = "https://dev-api.aioneers.tech/v1/trackingObjects"
    data = {
        "name": DOT_name,
        "description": DOT_description,
        "type": DOT_type,
        "baseline": DOT_baseline,
        "metricType": "5fb7bf2f8ce87f0012fcc8f3",
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, json=data, headers=headers)
    return response
