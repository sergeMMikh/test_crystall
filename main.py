from dotenv import load_dotenv
import os

from authorization import authorization, base_url, super_tocken, treiner_tocken
from lessons import create_check_list, get_all_lessons, create_lesson, get_all_check
from students import get_all_students, register_students
from check import create_check_list, get_list_of_check

load_dotenv()




def main():
    # Получение токена для дальнейшей работы
    authorize = super_tocken()

    if authorize != 'Error':
        token = authorize
    else:
        exit(1)

    # # Получение списка всех студентов
    # get_all_students(base_url=base_url,
    #                  token=token)

    # # Регистрация студентов
    # register_students(base_url=base_url,
    #                   token=token,
    #                   email='student6',
    #                   firstname='student6',
    #                   lastname='studentov6',
    #                   surname='studentovich6',
    #                   birthday='2020-06-')

    # Создание занятия
    # create_lesson(base_url=base_url,
    #               token=token)

    # Получение токена для дальнейшей работы
    authorize = treiner_tocken()
    
    if authorize != 'Error':
        token = authorize
    else:
        exit(1)

    # Получение всех занятий
    get_all_lessons(base_url=base_url,
                    token=token)
    
    # create_check_list(
    #     base_url=base_url,
    #     token=token)

    # Получение всех check для тренера
    get_all_check(base_url=base_url,
                      token=token)
    
    # Получение всех check для супера
    get_all_check(base_url=base_url,
                      token=super_tocken())

if __name__ == "__main__":
    main()
