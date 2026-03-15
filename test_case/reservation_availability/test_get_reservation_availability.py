import pytest
import allure
from api_requests.reservation_availability.Reservation_AvailabilityClient import Reservation_AvailabilityClient
from conftest import SERVER, RESTAURANT_CODE  

pytestmark = [pytest.mark.api, pytest.mark.check_reservation_availability]

EXPECTED_RESPONSE = {
    "availabilities": [
        {
            "restaurant_code": RESTAURANT_CODE,
            "is_available": False,
            "cached_at": 1738693875784
        }
    ],
    "msg_code": 0
}

@pytest.fixture
def get_reservation_availability_client(access_token):
    return Reservation_AvailabilityClient(token=access_token)

@allure.feature("Reservation Module")
@allure.story("Get Reservation Availability")
@allure.title("TC_RRA_001 - Verify response status and basic message code")
def test_TC_RRA_001_response_structure(get_reservation_availability_client):
    # 這裡建議檢查 status_code 時，如果不存在可以預設 None 或 0，避免誤判
    data = get_reservation_availability_client.get_reservation_availability_response()
    status_code = data.get("status_code", 200)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    assert "msg_code" in data, "Response missing 'msg_code'"
    assert data["msg_code"] == 0, "msg_code should be 0"

@allure.feature("Reservation Module")
@allure.story("Get Reservation Availability")
@allure.title("TC_RRA_002 - Verify data fields in availabilities list")
def test_TC_RRA_002_content(get_reservation_availability_client):
    data = get_reservation_availability_client.get_reservation_availability_response()
    assert "availabilities" in data, "Response missing 'availabilities'"
    reservation_info_list = data.get('availabilities', [])
    
    for reservation_info in reservation_info_list:
        assert "restaurant_code" in reservation_info, "Missing 'restaurant_code'"
        assert "is_available" in reservation_info, "Missing 'is_available'"
        assert "cached_at" in reservation_info, "Missing 'cached_at'"

@allure.feature("Reservation Module")
@allure.story("Get Reservation Availability")
@allure.title("TC_RRA_003 - Verify specific availability data content")
def test_TC_RRA_003_data(get_reservation_availability_client):
    data = get_reservation_availability_client.get_reservation_availability_response()
    response_list = data.get('availabilities', [])
    expected_list = EXPECTED_RESPONSE.get("availabilities", [])
    expected_entry = expected_list[0] 
    
    found = False
    for info in response_list:
        if (info["restaurant_code"] == expected_entry["restaurant_code"] and
            info["is_available"] == expected_entry["is_available"]):
            found = True
            break  

    assert found, f"Target data with restaurant_code {expected_entry['restaurant_code']} not found"