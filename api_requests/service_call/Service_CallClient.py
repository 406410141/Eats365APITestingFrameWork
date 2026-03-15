import requests
from conftest import SERVER, RESTAURANT_CODE  
from api_requests.base import BaseAPI
class Service_CallClient(BaseAPI):

    def get_service_call_list(self):
        endpoint = "/v2/service-call/list"
        params = {"restaurant_code": RESTAURANT_CODE}
        return self.get(endpoint, params=params)
