import requests
from conftest import SERVER, RESTAURANT_CODE  
from api_requests.base import BaseAPI

class ProductTypeClient(BaseAPI):

    def get_product_type_list(self):
        endpoint = "/v2/product-type/list"
        params = {"restaurant_code": RESTAURANT_CODE}

        return self.get(endpoint, params=params)

    
