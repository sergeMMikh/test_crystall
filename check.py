import requests
from pprint import pprint

def get_list_of_check(base_url: str, token: str):
    response = requests.get(
        url=f'{base_url}check',
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