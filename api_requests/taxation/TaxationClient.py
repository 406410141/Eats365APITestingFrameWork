import requests
from conftest import SERVER, RESTAURANT_CODE 
from api_requests.base import BaseAPI   


class TaxationClient(BaseAPI):
    def tax_type_response(self):

        endpoint = "/v2/taxation/tax-type/list"
        params = {"restaurant_code": RESTAURANT_CODE}
        return self.get(endpoint, params=params)
    
    def tax_group_response(self):
        endpoint = "/v2/taxation/tax-group/list"
    
        params = {"restaurant_code": RESTAURANT_CODE}
        return self.get(endpoint, params=params)
