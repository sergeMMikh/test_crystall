import requests
from pprint import pprint


def get_all_students(base_url: str, token: str):
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


def register_students(base_url: str,
                      token: str,
                      email: str,
                      firstname: str,
                      lastname: str,
                      surname: str,
                      birthday: str):
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
            "birthday": f"{birthday}{10 + i:02}T15:41:16.490Z",
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
