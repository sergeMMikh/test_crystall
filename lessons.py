import requests
from pprint import pprint

def create_space(base_url: str, token: str, name: str):
    response = requests.post(
        url=f'{base_url}space/?page_number=0&page_size=10',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {token}'
        },
        json={
            "name": name
        },
        )
    


    if response.status_code == 200:
        data = response.json()
        print("Response:")
        pprint(data)
        return 'ok'
    else:
        print(f'Error: {response.status_code}, {response.text}')
        return 'Error'

def get_all_lessons(base_url: str, token: str):
    response = requests.get(
        url=f'{base_url}lesson/?page_number=0&page_size=10',
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


def create_lesson(base_url: str,
                  token: str, 
                  space_id: int):
    register_url = f'{base_url}lesson/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    print("create_lesson")

    lesson_data = {
        "space_id": space_id,
        "trainer_id": 1,
        "trainer_comments": "message",
        "start": "2024-11-15T16:39:40.975Z"
    }

    # Отправка POST-запроса для регистрации студента
    response = requests.post(
        url=register_url,
        headers=headers,
        json=lesson_data
    )

    # Проверка ответа
    if response.status_code == 200:
        print(f"Lesson registered successfully.")
        pprint(response.json())
    else:
        print(f'Error creating lesson: {response.status_code}, {response.text}')


def create_check_list(base_url: str, token: str):
    # Cозданиt чек-листа
    register_url = f'{base_url}check/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Данные для создания чек-листа
    lesson_data = { 
        "students_id": [4, 5, 6],  # Используйте существующие ID студентов
        "lesson_id": 1,
        "training_check": [
            {"training_id": 1, "repetitions": 5},
            {"training_id": 2, "repetitions": 8}
        ]    
    }

    
    # Отправка POST-запроса
    response = requests.post(
        url=register_url,
        headers=headers,
        json=lesson_data
    )

    # Проверка ответа
    if response.status_code == 200:
        print("Check-list created successfully.")
        pprint(response.json())
    else:
        print(f'Error creating check-list: {response.status_code}, {response.text}')


def get_all_check(base_url: str, token: str):
    # payload = {
    #     "lesson_id": None,  # Или укажите ID урока, например, 1
    #     "student_id": None  # Или укажите ID студента, например, 1
    # }

    payload = {
        "lesson_id": 1,  # Или укажите ID урока, например, 1
        "student_id": 2  # Или укажите ID студента, например, 1
    }

    response = requests.get(
        url=f'{base_url}check/list',
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        },
        json=payload
        )

    if response.status_code == 200:
        data = response.json()
        print("Response:")
        pprint(data)
        return 'ok'
    else:
        print(f'Error: {response.status_code}, {response.text}')
        return 'Error'
    