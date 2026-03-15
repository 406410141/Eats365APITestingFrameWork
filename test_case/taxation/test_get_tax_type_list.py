import pytest
import allure
from api_requests.taxation.TaxationClient import TaxationClient

# 套用 pytest.ini 中的標籤
pytestmark = [pytest.mark.api, pytest.mark.tax_type]

@pytest.fixture
def get_tax_type_response_client(access_token):
    return TaxationClient(token=access_token)

EXPECTED_TAX_TYPE = {
    "id": 3007,
    "name": "萬萬稅",
    "rate": 5,
    "is_dine_in_enabled": True,
    "is_takeout_enabled": True
}

@allure.feature("Taxation Module")
@allure.story("Tax Type")
@allure.title("TC_TT_001 - Verify tax type response structure and status")
def test_TC_TT_001_structure(get_tax_type_response_client):
    data = get_tax_type_response_client.tax_type_response()
    # 修正變數名稱以符合 Fixture
    status_code = data.get('status_code', 200)
    assert status_code == 200, f"Expected 200, but got {status_code}"
    assert "version" in data, "Response missing 'version'"
    assert "msg_code" in data, "Response missing 'msg_code'"
    assert data["version"] > 0, "version should be > 0"
    assert data["msg_code"] == 0, "msg_code should be 0"

@allure.feature("Taxation Module")
@allure.story("Tax Type")
@allure.title("TC_TT_002 - Verify tax type list content and mandatory fields")
def test_TC_TT_002_structure(get_tax_type_response_client):
    data = get_tax_type_response_client.tax_type_response()
    assert "tax_type_list" in data, "Response missing 'tax_type_list'"
    tax_type_list = data.get("tax_type_list", [])
    assert len(tax_type_list) > 0, "tax_type_list should not be empty"
    for tax_type in tax_type_list:
        assert "id" in tax_type, "Tax type missing 'id'"
        assert "name" in tax_type, "Tax type missing 'name'"
        assert "rate" in tax_type, "Tax type missing 'rate'"
        assert "is_dine_in_enabled" in tax_type, "Tax type missing 'is_dine_in_enabled'"
        assert "is_takeout_enabled" in tax_type, "Tax type missing 'is_takeout_enabled'"

@allure.feature("Taxation Module")
@allure.story("Tax Type")
@allure.title("TC_TT_003 - Verify specific tax type data accuracy")
def test_TC_TT_003_data(get_tax_type_response_client):
    data = get_tax_type_response_client.tax_type_response()
    tax_type_list = data.get("tax_type_list", [])
    found = False
    for tax_type in tax_type_list:
        if (tax_type["id"] == EXPECTED_TAX_TYPE["id"] and 
            tax_type["name"] == EXPECTED_TAX_TYPE["name"] and
            tax_type["rate"] == EXPECTED_TAX_TYPE["rate"] and
            tax_type["is_dine_in_enabled"] == EXPECTED_TAX_TYPE["is_dine_in_enabled"] and
            tax_type["is_takeout_enabled"] == EXPECTED_TAX_TYPE["is_takeout_enabled"]):
                found = True
                break
    assert found, f"Expected tax type data with ID {EXPECTED_TAX_TYPE['id']} not found"