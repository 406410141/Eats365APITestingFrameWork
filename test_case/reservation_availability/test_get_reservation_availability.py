import pytest
import allure
from api_requests.reservation_availability.get_reservation_availability import get_reservation_availability_response
from conftest import SERVER, RESTAURANT_CODE  


EXPECTED_RESPONSE ={
    "availabilities": [
        {
            "restaurant_code":RESTAURANT_CODE,
            "is_available": False,
            "cached_at": 1738693875784
        }
    ],
    "msg_code": 0
}

@pytest.fixture
def get_reservation_availability_fixture(access_token):
    return get_reservation_availability_response(access_token)  


@pytest.mark.api
@pytest.mark.check_reservation_availability
@pytest.mark.TC_RRA_001
def test_reservation_availability_response_structure(get_reservation_availability_fixture):
    assert get_reservation_availability_fixture.get("status_code",200) ==200,f"Expected status code 200, but got {get_reservation_availability_fixture.get('status_code')}"
    assert "msg_code" in get_reservation_availability_fixture , "Response missing 'msg_code'"
    assert get_reservation_availability_fixture["msg_code"] == 0 ,  "msg_code should be 0"


@pytest.mark.api
@pytest.mark.check_reservation_availability
@pytest.mark.TC_RRA_002
def test_reservation_availability_content(get_reservation_availability_fixture):
    assert "availabilities" in get_reservation_availability_fixture , "Response missing 'availabilities'"
    reservation_info_list =  get_reservation_availability_fixture.get('availabilities')
    #print(reservation_info)
    for reservation_info in reservation_info_list:
        assert "restaurant_code" in reservation_info, "Response missing 'restaurant_code'"
        assert "is_available" in reservation_info, "Response missing 'is_available'"
        assert "cached_at" in reservation_info, "Response missing 'cached_at'"



@pytest.mark.api
@pytest.mark.check_reservation_availability_data
@pytest.mark.TC_RRA_003
def test_reservation_availability_data(get_reservation_availability_fixture):
    response_list = get_reservation_availability_fixture.get('availabilities', [])
    expected_list = EXPECTED_RESPONSE.get("availabilities", [])
    expected_entry = expected_list[0] 
    found = False
    for info in response_list:
        if (info["restaurant_code"] == expected_entry["restaurant_code"] and
            info["is_available"] == expected_entry["is_available"]):
            found = True
            break  

    assert found, f"Expected response data with restaurant_code {expected_entry['restaurant_code']} not found"
