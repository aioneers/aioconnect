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
