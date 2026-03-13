import requests
from conftest import SERVER, RESTAURANT_CODE  

def get_reservation_availability_response(access_token):
    url = f"{SERVER}/v2/reservation/availability/check"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    json = {
            "party_size": 6,
            "reservation_timestamp": 1737039620000,
            "restaurant_code_list": [
                RESTAURANT_CODE
            ]
}
    response = requests.post(url, headers=headers, json=json)
    assert response.status_code == 200, f"Former Employee failed: {response.text}"
    return response.json()  # Return the JSON response