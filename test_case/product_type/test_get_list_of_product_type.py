import pytest
import allure
from api_requests.product_type.Product_TypeClient import ProductTypeClient 

pytestmark = [pytest.mark.api, pytest.mark.product_type]

@pytest.fixture
def get_product_type_client(access_token):
    return ProductTypeClient(token=access_token)

EXPECTED_PRODUCT_TYPES = {
    1: "一般",
    2: "食物",
    3: "飲品"
}

@allure.feature("Product Module")
@allure.story("Product Type List")
@allure.title("TC_PT_001 - Verify response structure and basic fields")
@allure.description("This is description")
def test_TC_PT_001_response_structure(get_product_type_client):
    # 僅修正原本的 test＿TC (全形) 為 test_TC (半形)
    data = get_product_type_client.get_product_type_list() 
    assert "version" in data, "Response missing 'version'"
    assert "msg_code" in data, "Response missing 'msg_code'"
    # 保持你原本的邏輯
    assert data["msg_code"] == 1, "msg_code should be 1"
    assert data["version"] > 0, "version should be greater than 0"

@allure.feature("Product Module")
@allure.story("Product Type List")
@allure.title("TC_PT_002 - Verify existence of name and ID fields")
def test_TC_PT_002_has_name_and_id(get_product_type_client):
    data = get_product_type_client.get_product_type_list()
    assert "product_type_list" in data, "Response missing 'product_type_list'"
    product_type_list = data.get("product_type_list", [])

    for product_type in product_type_list:
        assert "id" in product_type, "Product type missing 'id'"
        assert "name" in product_type, "Product type missing 'name'"
        assert isinstance(product_type["name"], dict), "'name'  should be a dict"
        assert len(product_type["name"]) > 0, "'name' should not be empty"

@allure.feature("Product Module")
@allure.story("Product Type List")
@allure.title("TC_PT_003 - Verify nested sub-type list structure")
def test_TC_PT_003_sub_type_structure(get_product_type_client):
    data = get_product_type_client.get_product_type_list()
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

@allure.feature("Product Module")
@allure.story("Product Type List")
@allure.title("TC_PT_004 - Verify Traditional Chinese name content accuracy")
def test_TC_PT_004_content(get_product_type_client):
    data = get_product_type_client.get_product_type_list()
    product_type_list = data.get("product_type_list", [])
    
    id_name_map = {item["id"]: item["name"].get("zh_TW") for item in product_type_list if "id" in item and "name" in item}

    for expected_id, expected_name in EXPECTED_PRODUCT_TYPES.items():
        assert expected_id in id_name_map, f" Missing Product Type ID {expected_id}"
        assert id_name_map[expected_id] == expected_name, f"ID {expected_id} name error , expected : {expected_name}，actual: {id_name_map.get(expected_id)}"