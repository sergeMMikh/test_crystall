import requests
from pprint import pprint
from dotenv import load_dotenv
import os

url = 'http://172.31.60.129:8001/api/v1/auth/login/'

load_dotenv()

base_url = 'http://172.31.60.129:8001/api/v1/'


def main():
    print(f"username: {os.getenv('APP_USERNAME')}")
    response = requests.post(
        # url=url,
        url=f'{base_url}auth/login/',
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

        token = data.get('access_token')
        print(f'token: {token}')
    else:
        print(f'Error: {response.status_code}, {response.text}')
        exit(1)

    response = requests.get(
        # url='http://localhost:8001/api/v1/student/?page_number=0&page_size=10',
        url=f'{base_url}student/?page_number=0&page_size=10',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {token}'
        })

    if response.status_code == 200:
        data = response.json()
        print("Response:")
        pprint(data)

    else:
        print(f'Error: {response.status_code}, {response.text}')
        exit(1)

    # register_url = 'http://localhost:8001/api/v1/user/register/'
    register_url = f'{base_url}user/register/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    num_students = 10

    for i in range(num_students):
        # Форматирование данных для каждого студента с уникальными значениями на основе итератора i
        student_data = {
            "email": f"student2{i}@example.com",
            "password": f"passwd2{i}",
            "firstname": f"student2{i}",
            "lastname": f"studentov2{i}",
            "surname": f"studentovich2{i}",
            "birthday": f"2020-10-{10 + i:02}T15:41:16.490Z",  # уникальная дата на основе i
            "is_man": True,
            "contact": "string"
        }

        # Отправка POST-запроса для регистрации студента
        response = requests.post(
            url=register_url,
            headers=headers,
            json=student_data
        )

        # Проверка ответа
        if response.status_code == 200:
            print(f"Student {i} registered successfully.")
            pprint(response.json())
        else:
            print(f'Error registering student {i}: {response.status_code}, {response.text}')


if __name__ == "__main__":
    main()
