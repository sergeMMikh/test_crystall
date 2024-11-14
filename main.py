import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

base_url = 'http://172.31.60.129:8001/api/v1/'


def authorization(username: str, password: str) -> str:
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


def get_all_students(token):
    response = requests.get(
        url=f'{base_url}student/?page_number=0&page_size=10',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {token}'
        })

    if response.status_code == 200:
        data = response.json()
        print("Response:")
        pprint(data)
        return 'ok'
    else:
        print(f'Error: {response.status_code}, {response.text}')
        return 'Error'


def register_students(token, email, firstname, lastname, surname, birthday):
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
            "email": f"{email}{i}@example.com",
            "password": f"passwd2{i}",
            "firstname": f"{firstname}{i}",
            "lastname": f"{lastname}{i}",
            "surname": f"{surname}{i}",
            "birthday": f"2020-12-{10 + i:02}T15:41:16.490Z",
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


def main():
    authorize = authorization(username=os.getenv('APP_USERNAME'),
                              password=os.getenv('APP_PASSWORD'))

    if authorize != 'Error':
        token = authorize
    else:
        exit(1)

    get_all_students(token=token)

    register_students(token=token,
                      email='student4',
                      firstname='student4',
                      lastname='studentov4',
                      surname='studentovich4',
                      birthday='2020-05-')


if __name__ == "__main__":
    main()
