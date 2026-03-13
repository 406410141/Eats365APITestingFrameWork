import requests
from conftest import SERVER, RESTAURANT_CODE 


def tax_type_response(access_token):
    """Get Tax Type API Response"""
    url = f"{SERVER}/v2/taxation/tax-type/list"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    params = {"restaurant_code": RESTAURANT_CODE}
    response = requests.get(url, headers=headers, params=params)
    return response.json()