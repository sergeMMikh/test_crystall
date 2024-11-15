import requests
from pprint import pprint


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
                  token: str):
    register_url = f'{base_url}lesson/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    lesson_data = {
        "space_id": 1,
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
    # Правильный URL для создания чек-листа
    register_url = f'{base_url}lesson/create-check/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Данные для создания чек-листа
    lesson_data = { 
        "student_ids": [4, 5, 6],  # Используйте существующие ID студентов
        "lesson_id": 2,
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
