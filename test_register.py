import sys
sys.path.insert(0, str(sys.path[0] + "\\lib"))

import requests

API_URL = "http://127.0.0.1:8003/register"
data = {
    "full_name": "Test User",
    "email": "test@example.com",
    "password": "testpass123"
}

print(f"Testing API at {API_URL}...")
print("Sending data:", data)

try:
    response = requests.post(API_URL, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")  # Show raw text instead of trying to parse JSON
except Exception as e:
    print(f"Error: {e}")
    import traceback
    print(traceback.format_exc())
