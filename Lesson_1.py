#1
import requests
import json

params = {'q': 'name', 'id': '69846294'}
url = 'https://api.github.com'
user = 'TIMUR643'
responce = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(responce.json(), f)
    
for i in responce.json():
    print(i['full_name'])
    
    #2
    
import requests
import sys
import json

URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=e4d256314b984424bb9122029222302&q=London&fx=no&cc=no&mca=yes&format=xml'

def _main():
    """Entry point."""
    req = requests.get(URL + '/getMe')

    with open('data_2.json', 'w') as f_obj:
        json.dump(req.text, f_obj)


if __name__ == '__main__':
    sys.exit(_main())
