import requests
from pprint import pprint

base_url = 'http://127.0.0.1:8000/api/v1/'

def authorization(base_url: str, username: str, password: str) -> str:
    response = requests.post(
        # url=url,
        url=f'{base_url}auth/login/',
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'grant_type': 'password',
            'username': username,
            'password': password,
            'scope': '',
            'client_id': 'string',
            'client_secret': 'string'
        }
    )

    if response.status_code == 200:
        data = response.json()
        print("Response:")
        pprint(data)

        token = data.get('access_token')
        print(f'token: {token}')
        return token
    else:
        print(f'Error: {response.status_code}, {response.text}')
        return 'Error'


def treiner_tocken():
    return authorization(
        base_url=base_url,
        # username=os.getenv('APP_USERNAME'),
        # password=os.getenv('APP_PASSWORD'))
        username='trainer@crystal.com',
        password='trainerpass')

def super_tocken():
    return authorization(
        base_url=base_url,
        # username=os.getenv('APP_USERNAME'),
        # password=os.getenv('APP_PASSWORD'))
        username='supervisor@crystal.com',
        password='supervisorpass')