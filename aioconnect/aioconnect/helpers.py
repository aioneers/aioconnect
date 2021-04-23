"""Extract nested values from a JSON tree."""


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


def get_objects(url,headers,payload,feature):
    list1=[]
    response = json.loads((requests.request("GET", url, headers=headers, data=payload)).text)['data']['payload']
    response.raise_for_status()
    count = len(response)
    for i in range(0,count):
        x = response[i][feature]
        list1.append(x)
    return list1