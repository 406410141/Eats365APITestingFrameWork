import pytest
import allure
from api_requests.taxation.TaxationClient import TaxationClient

# 套用 pytest.ini 中的標籤
pytestmark = [pytest.mark.api, pytest.mark.tax_group]

@pytest.fixture
def get_tax_group_response_client(access_token):
    return TaxationClient(token=access_token)

EXPECTED_TAX_GROUP = {
    "id": 2620,
    "name": "Tax For API Testing",
    "tax_type_id_list": [3249, 3007]
}

@allure.feature("Taxation Module")
@allure.story("Tax Group")
@allure.title("TC_TG_001 - Verify tax group response structure and status")
def test_TC_TG_001_structure(get_tax_group_response_client):
    data = get_tax_group_response_client.tax_group_response()
    status_code = data.get('status_code', 200)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    assert "msg_code" in data, "Response missing 'msg_code'"
    assert data["msg_code"] == 0, "msg_code should be 0"

@allure.feature("Taxation Module")
@allure.story("Tax Group")
@allure.title("TC_TG_002 - Verify tax group list content and data types")
def test_TC_TG_002_content(get_tax_group_response_client):
    data = get_tax_group_response_client.tax_group_response()
    assert "tax_group_list" in data, "Response missing 'tax_group_list'"
    tax_group_list = data.get("tax_group_list", [])
    assert len(tax_group_list) > 0, "tax_group_list should not be empty"
    for tax_group in tax_group_list:
        assert "id" in tax_group, "Tax group missing 'id'"
        assert "name" in tax_group, "Tax group missing 'name'"
        assert "tax_type_id_list" in tax_group, "Tax group missing 'tax_type_id_list'"
        assert isinstance(tax_group["tax_type_id_list"], list), "'tax_type_id_list' should be a list"
        assert len(tax_group["tax_type_id_list"]) > 0, "tax_type_id_list should not be empty"

@allure.feature("Taxation Module")
@allure.story("Tax Group")
@allure.title("TC_TG_003 - Verify specific tax group data accuracy")
def test_TC_TG_003_data(get_tax_group_response_client):
    data = get_tax_group_response_client.tax_group_response()
    tax_group_list = data.get("tax_group_list", [])
    found = False
    for tax_group in tax_group_list:
        if (tax_group["id"] == EXPECTED_TAX_GROUP["id"] and 
            tax_group["name"] == EXPECTED_TAX_GROUP["name"] and
            tax_group["tax_type_id_list"] == EXPECTED_TAX_GROUP["tax_type_id_list"]):
            found = True
            break
    
    assert found, f"Expected tax group data with ID {EXPECTED_TAX_GROUP['id']} not found"