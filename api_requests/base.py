import requests
import allure
from conftest import SERVER

class BaseAPI:
    def __init__(self, token=None):
        self.base_url = SERVER
        self.headers = {"Content-Type": "application/json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def _send_request(self, method, endpoint, params=None, json=None):

        url = f"{self.base_url}{endpoint}"
        

        with allure.step(f"Sending {method} request to {endpoint}"):
            response = requests.request(
                method=method, 
                url=url, 
                headers=self.headers, 
                params=params, 
                json=json      
            )
            
    
            print(f"\n[{method}] {response.url}")
            if json:
                print(f"Payload: {json}")
                
            return response.json()


    def get(self, endpoint, params=None, json=None):
        return self._send_request("GET", endpoint, params=params, json=json)

    def post(self, endpoint, params=None, json=None):
        return self._send_request("POST", endpoint, params=params, json=json)

    def put(self, endpoint, params=None, json=None):
        return self._send_request("PUT", endpoint, params=params, json=json)

    def delete(self, endpoint, params=None, json=None):
        return self._send_request("DELETE", endpoint, params=params, json=json)
    
    def patch(self, endpoint, params=None, json=None):
        return self._send_request("PATCH", endpoint, params=params, json=json)
