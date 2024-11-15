from dotenv import load_dotenv
import os

from authorization import authorization
from lessons import get_all_lessons, create_lesson
from students import get_all_students, register_students

load_dotenv()

base_url = 'http://172.31.60.129:8001/api/v1/'


def main():
    # Получение токена для дальнейшей работы
    authorize = authorization(
        base_url=base_url,
        username=os.getenv('APP_USERNAME'),
        password=os.getenv('APP_PASSWORD'))

    if authorize != 'Error':
        token = authorize
    else:
        exit(1)

    # Получение списка всех студентов
    # get_all_students(base_url=base_url,
    #                  token=token)

    # Регистрация студентов
    # register_students(base_url=base_url,
    #                   token=token,
    #                   email='student5',
    #                   firstname='student5',
    #                   lastname='studentov5',
    #                   surname='studentovich5',
    #                   birthday='2020-06-')

    # Создание занятия
    # create_lesson(base_url=base_url,
    #               token=token)

    # Получение всех занятий
    get_all_lessons(base_url=base_url,
                    token=token)




if __name__ == "__main__":
    main()
