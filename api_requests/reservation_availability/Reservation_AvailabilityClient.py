import requests
from conftest import SERVER, RESTAURANT_CODE  
from api_requests.base import BaseAPI   
class Reservation_AvailabilityClient(BaseAPI):

    def get_reservation_availability_response(self):
            endpoint = "/v2/reservation/availability/check"
            params = {"restaurant_code": RESTAURANT_CODE}
            payload = {
                "party_size": 6,
                "reservation_timestamp": 1737039620000,
                "restaurant_code_list": [
                    RESTAURANT_CODE
                ]
                    }
            return self.post(endpoint, params= params, json=payload)


