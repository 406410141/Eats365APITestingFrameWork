import requests
from conftest import SERVER, RESTAURANT_CODE 

def tax_group_response(access_token):
    """Get Tax Group API Response"""
    url = f"{SERVER}/v2/taxation/tax-group/list"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    params = {"restaurant_code": RESTAURANT_CODE}
    response = requests.get(url, headers=headers, params=params)
    return response.json()  
