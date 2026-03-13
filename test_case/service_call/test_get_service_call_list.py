import pytest
from api_requests.service_call.get_service_call_list import get_service_call_list  # type: ignore

@pytest.fixture
def get_service_call_list_fixture(access_token):
    return get_service_call_list(access_token)  


EXPECTED_SERVICE_CALL = {
            "id": 780,
            "name": {
                "zh_TW": "裝水水"
            }
}


@pytest.mark.api
@pytest.mark.service_call
@pytest.mark.TC_SC_001 
def test_service_call_response_structure(get_service_call_list_fixture):
    assert get_service_call_list_fixture.get('status_code', 200) == 200, f"Expected status code 200, but got {service_call_response.get('status_code')}"
    assert "version" in get_service_call_list_fixture, "Response missing 'version'"
    assert "msg_code" in get_service_call_list_fixture, "Response missing 'msg_code'"
    assert get_service_call_list_fixture["version"]  > 0, "version should be > 0"
    assert get_service_call_list_fixture["msg_code"] == 0, "msg_code should be 0"


@pytest.mark.api
@pytest.mark.service_call
@pytest.mark.TC_SC_002
def test_service_call_content(get_service_call_list_fixture):
    assert "service_call_list" in get_service_call_list_fixture, "Response missing 'service_call_list'"
    service_call_list = get_service_call_list_fixture.get("service_call_list",[])
    assert len(service_call_list) > 0  
    for service_call in service_call_list:
        assert "id" in service_call, "Service Call missing 'id'"
        assert "name" in service_call, "Service Call missing 'name'"




@pytest.mark.api
@pytest.mark.service_call
@pytest.mark.TC_SC_003
def test_service_call_data(get_service_call_list_fixture):
    service_call_list = get_service_call_list_fixture.get("service_call_list", [])
    
    found = False
    for service_call in service_call_list:
        if (service_call["id"] == EXPECTED_SERVICE_CALL["id"] and 
            service_call["name"] == EXPECTED_SERVICE_CALL["name"]):
            found = True
            break
    
    assert found, f"Expected Service Call data with ID {EXPECTED_SERVICE_CALL['id']} not found"













