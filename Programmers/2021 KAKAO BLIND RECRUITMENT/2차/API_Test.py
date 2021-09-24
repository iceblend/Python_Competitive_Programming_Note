# API 테스트?
# https://httpbin.org/#/
# https://twpower.github.io/124-python-requests-usage
# https://velog.io/@euzl/Python-requests%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-REST-API-%ED%86%B5%EC%8B%A0-%EC%9D%BC%EB%B6%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EB%B2%95

'''import requests

base_url = "https://httpbin.org/"
#x_auth_token = "811b6d6184d6760f19d512737be051bb"

res = requests.get(base_url)
print(res)
'''

import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://httpbin.org/get')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')