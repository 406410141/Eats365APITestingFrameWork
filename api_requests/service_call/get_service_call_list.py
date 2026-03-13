import requests
from conftest import SERVER, RESTAURANT_CODE  


def get_service_call_list(access_token):
    url = f"{SERVER}/v2/service-call/list"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    params = {"restaurant_code": RESTAURANT_CODE}
    response = requests.get(url, headers=headers, params=params)
    return response.json()  