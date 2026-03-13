import requests

SERVER = "https://dev.eats365pos.net"

def get_access_token():
    """Get API Access Token"""
    url = f"{SERVER}/o/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
        }
    request_body = {
        "client_id": "41e43d3896ed4b2397d0015caff6bcee",
        "grant_type": "client_credentials",
        "client_secret": "6f78606909e144b2a39516b2a291dc3cb3fcfb60107c4711879a7655a500eb48"
    }
    response = requests.post(url, headers=headers, data=request_body)
    
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get access token: {response.text}")