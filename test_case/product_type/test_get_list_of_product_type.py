import pytest
import allure
from api_requests.product_type.get_product_type_list import get_product_type_list 

@pytest.fixture
def get_product_type_list_fixture(access_token):
    return get_product_type_list(access_token)  


EXPECTED_PRODUCT_TYPES = {
    1: "一般",
    2: "食物",
    3: "飲品"
}

@pytest.mark.api
@pytest.mark.product_type
@pytest.mark.TC_PT_001  
@allure.title("This is title")
@allure.description("This is discritpion")
@allure.feature("productype")
@allure.story("Get  Product Type list")
def test_product_type_response_structure(get_product_type_list_fixture):
    data = get_product_type_list_fixture 
    assert "version" in data, "Response missing 'version'"
    assert "msg_code" in data, "Response missing 'msg_code'"
    #wrong point 
    assert data["msg_code"] == 1, "msg_code should be 1"
    assert data["version"] > 0, "version should be greater than 0"

@pytest.mark.api
@pytest.mark.product_type
@pytest.mark.TC_PT_002  
def test_product_type_list_has_name_and_id(get_product_type_list_fixture):
    data = get_product_type_list_fixture 
    assert "product_type_list" in data, "Response missing 'product_type_list'"
    product_type_list = data.get("product_type_list", [])

    for product_type in product_type_list:
        assert "id" in product_type, "Product type missing 'id'"
        assert "name" in product_type, "Product type missing 'name'"
        assert isinstance(product_type["name"], dict), "'name'  should be a dict"
        assert len(product_type["name"]) > 0, "'name' should not be empty"

@pytest.mark.api
@pytest.mark.product_type
@pytest.mark.TC_PT_003
def test_product_type_sub_type_structure(get_product_type_list_fixture):
    data = get_product_type_list_fixture 
    product_type_list = data.get("product_type_list", [])

    for product_type in product_type_list:
        assert "id" in product_type, "Product type missing 'id'"
        assert "name" in product_type, "Product type missing 'name'"
        assert isinstance(product_type["name"], dict), "'name' should be a dict"

        # check sub type
        for sub_type in product_type.get("sub_type_list", []):
            assert "id" in sub_type, "Sub type missing 'id'"
            assert "name" in sub_type, "Sub type missing 'name'"
            assert isinstance(sub_type["name"], dict), "'name' in sub_type should be a dict"

@pytest.mark.api
@pytest.mark.product_type
@pytest.mark.TC_PT_004
@allure.title("Sub product type")
def test_product_type_list_content(get_product_type_list_fixture):

    data = get_product_type_list_fixture 
    product_type_list = data.get("product_type_list", [])
    
    id_name_map = {item["id"]: item["name"].get("zh_TW") for item in product_type_list if "id" in item and "name" in item}


    for expected_id, expected_name in EXPECTED_PRODUCT_TYPES.items():
        assert expected_id in id_name_map, f" Missing Product Type ID {expected_id}"
        assert id_name_map[expected_id] == expected_name, f"ID {expected_id} name error , expected : {expected_name}，actual: {id_name_map.get(expected_id)}"