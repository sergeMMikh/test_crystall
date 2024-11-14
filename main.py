import requests
from pprint import pprint
from dotenv import load_dotenv
import os

url = 'http://172.31.60.129:8001/api/v1/auth/login/'

load_dotenv()


def main():
    print(f"username: {os.getenv('APP_USERNAME')}")
    response = requests.post(
        url=url,
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'grant_type': 'password',
            'username': os.getenv('APP_USERNAME'),
            'password': os.getenv('APP_PASSWORD'),
            'scope': '',
            'client_id': 'string',
            'client_secret': 'string'
        }
    )

    if response.status_code == 200:
        data = response.json()
        print("Response:")
        pprint(data)

        TOKEN = data.get('access_token')
        print(f'TOKEN: {TOKEN}')
    else:
        print(f'Error: {response.status_code}, {response.text}')
        exit(1)

    response = requests.get(
        url='http://localhost:8001/api/v1/student/?page_number=0&page_size=10',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {TOKEN}'
        })

    if response.status_code == 200:
        data = response.json()
        print("Response:")
        pprint(data)

    else:
        print(f'Error: {response.status_code}, {response.text}')
        exit(1)


if __name__ == "__main__":
    main()
