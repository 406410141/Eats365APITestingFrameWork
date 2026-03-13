import pytest
from utility.access_token import get_access_token

SERVER = "https://dev.eats365pos.net"
RESTAURANT_CODE = "TWTP000097"

@pytest.fixture(scope="module")
def access_token():
    """Get Access Token"""
    return get_access_token()