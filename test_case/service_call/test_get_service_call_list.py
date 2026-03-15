import pytest
import allure
from api_requests.service_call.Service_CallClient import Service_CallClient  # type: ignore
pytestmark = [pytest.mark.api, pytest.mark.service_call]

@pytest.fixture
def get_service_call_list_client(access_token):
    return Service_CallClient(token=access_token)




EXPECTED_SERVICE_CALL = {
            "id": 780,
            "name": {
                "zh_TW": "裝水水"
            }
}



@allure.feature("Service Call Module")
@allure.story("Get Service Call List")
@allure.title("TC_SC_001 - Verify response structure and basic fields")
def test_TC_SC_001_structure(get_service_call_list_client):
    # 修正：將變數名稱改為與參數一致
    data = get_service_call_list_client.get_service_call_list()
    status_code = data.get('status_code', 200)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    assert "version" in data, "Response missing 'version'"
    assert "msg_code" in data, "Response missing 'msg_code'"
    assert data["version"] > 0, "version should be > 0"
    assert data["msg_code"] == 0, "msg_code should be 0"


@allure.feature("Service Call Module")
@allure.story("Get Service Call List")
@allure.title("TC_SC_002 - Verify service call list content and mandatory fields")
def test_TC_SC_002_content(get_service_call_list_client):
    data = get_service_call_list_client.get_service_call_list()
    assert "service_call_list" in data, "Response missing 'service_call_list'"
    service_call_list = data.get("service_call_list",[])
    assert len(service_call_list) > 0  
    for service_call in service_call_list:
        assert "id" in service_call, "Service Call missing 'id'"
        assert "name" in service_call, "Service Call missing 'name'"


allure.feature("Service Call Module")
@allure.story("Get Service Call List")
@allure.title("TC_SC_003 - Verify specific service call data accuracy")
def test_TC_SC_003_data(get_service_call_list_client):
    data = get_service_call_list_client.get_service_call_list()
    service_call_list = data.get("service_call_list", [])
    
    found = False
    for service_call in service_call_list:
        if (service_call["id"] == EXPECTED_SERVICE_CALL["id"] and 
            service_call["name"] == EXPECTED_SERVICE_CALL["name"]):
            found = True
            break
    
    assert found, f"Expected Service Call data with ID {EXPECTED_SERVICE_CALL['id']} not found"













