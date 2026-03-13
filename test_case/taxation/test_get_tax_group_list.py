import pytest
from api_requests.taxation.get_tax_group_list import tax_group_response 


@pytest.fixture
def get_tax_group_response_fixture(access_token):
    return tax_group_response(access_token)  

EXPECTED_TAX_GROUP = {
    "id": 2620,
    "name": "Tax For API Testing",
    "tax_type_id_list": [3249, 3007]
}

@pytest.mark.api
@pytest.mark.tax_group
@pytest.mark.TC_TG_001 
def test_tax_group_response_structure(get_tax_group_response_fixture):
    assert get_tax_group_response_fixture.get('status_code', 200) == 200, f"Expected status code 200, but got {get_tax_group_response_fixture.get('status_code')}"
    assert "msg_code" in get_tax_group_response_fixture, "Response missing 'msg_code'"
    assert get_tax_group_response_fixture["msg_code"] == 0, "msg_code should be 0"


@pytest.mark.api
@pytest.mark.tax_group
@pytest.mark.TC_TG_002  
def test_tax_group_list_content(get_tax_group_response_fixture):
    tax_group_list = get_tax_group_response_fixture.get("tax_group_list", [])
    assert "tax_group_list" in get_tax_group_response_fixture, "Response missing 'tax_group_list'"
    assert len(tax_group_list) > 0, "tax_group_list should not be empty"
    for tax_group in tax_group_list:
        assert "id" in tax_group, "Tax group missing 'id'"
        assert "name" in tax_group, "Tax group missing 'name'"
        assert "tax_type_id_list" in tax_group, "Tax group missing 'tax_type_id_list'"
        assert isinstance(tax_group["tax_type_id_list"], list), "'tax_type_id_list' should be a list"
        assert len(tax_group["tax_type_id_list"]) > 0, "'tax_type_id_list' should contain at least one tax type ID"


@pytest.mark.api
@pytest.mark.tax_group
@pytest.mark.TC_TG_003 
def test_tax_group_data(get_tax_group_response_fixture):
    tax_group_list = get_tax_group_response_fixture.get("tax_group_list", [])
    found = False
    for tax_group in tax_group_list:
        if (tax_group["id"] == EXPECTED_TAX_GROUP["id"] and 
            tax_group["name"] == EXPECTED_TAX_GROUP["name"] and
            tax_group["tax_type_id_list"] == EXPECTED_TAX_GROUP["tax_type_id_list"]):
            found = True
            break
    
    assert found, f"Expected tax group data with ID {EXPECTED_TAX_GROUP['id']} not found"