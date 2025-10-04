# endpoint_test.py

import requests

try:
    resp = requests.get('http://127.0.0.1:5000/predictdata')
    assert resp.status_code == 200
    print(' /predictdata endpoint works')
except Exception as e:
    print(e)
    exit(1)
