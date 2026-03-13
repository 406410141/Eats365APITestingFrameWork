import pytest
from api_requests.taxation.get__tax_type_list import tax_type_response  

@pytest.fixture
def get_tax_type_response_fixture(access_token):
    return tax_type_response(access_token) 

EXPECTED_TAX_TYPE = {
    "id": 3007,
    "name": "萬萬稅",
    "rate": 5,
    "is_dine_in_enabled": True,
    "is_takeout_enabled": True
}


@pytest.mark.api
@pytest.mark.tax_type
@pytest.mark.TC_TT_001
def test_tax_type_response_structure(get_tax_type_response_fixture):
    assert get_tax_type_response_fixture.get('status_code', 200) == 200, f"Expected status code 200, but got {tax_type_response.get('status_code')}"
    assert "version" in get_tax_type_response_fixture, "Response missing 'version'"
    assert "msg_code" in get_tax_type_response_fixture, "Response missing 'msg_code'"


    assert get_tax_type_response_fixture["version"] > 0, "version should be > 0"

    assert get_tax_type_response_fixture["msg_code"] == 0, "msg_code should be 0"

@pytest.mark.api
@pytest.mark.tax_type
@pytest.mark.TC_TT_002
def test_tax_type_list_structure(get_tax_type_response_fixture):
    """TC_TT_002 - 驗證 tax_type_list """
    assert "tax_type_list" in get_tax_type_response_fixture, "Response missing 'tax_type_list'"
    tax_type_list = get_tax_type_response_fixture.get("tax_type_list",[])
    assert len(tax_type_list) > 0, "tax_type_list should not be empty"
    for tax_type in tax_type_list:
        assert "id" in tax_type, "Tax type missing 'id'"
        assert "name" in tax_type, "Tax type missing 'name'"
        assert "rate" in tax_type, "Tax type missing 'rate'"
        assert "is_dine_in_enabled" in tax_type, "Tax type missing 'is_dine_in_enabled'"
        assert "is_takeout_enabled" in tax_type, "Tax type missing 'is_takeout_enabled'"


@pytest.mark.api
@pytest.mark.tax_type
@pytest.mark.TC_TT_003
def test_tax_type_data(get_tax_type_response_fixture):
    tax_type_list = get_tax_type_response_fixture.get("tax_type_list",[])
    found = False
    for tax_type in tax_type_list:
        if (tax_type["id"] == EXPECTED_TAX_TYPE["id"] and 
            tax_type["name"] == EXPECTED_TAX_TYPE["name"] and
            tax_type["rate"] == EXPECTED_TAX_TYPE["rate"] and
            tax_type["is_dine_in_enabled"] == EXPECTED_TAX_TYPE["is_dine_in_enabled"] and
            tax_type["is_takeout_enabled"] == EXPECTED_TAX_TYPE["is_takeout_enabled"]):
                found = True
                break
    assert found, f"Expected tax group data with ID {EXPECTED_TAX_TYPE['id']} not found"