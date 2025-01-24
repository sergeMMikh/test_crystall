from dotenv import load_dotenv
import os

from authorization import authorization, base_url, super_tocken, treiner_tocken
from lessons import create_check_list, create_space, get_all_lessons, create_lesson, get_all_check
from students import get_all_students, register_students
from check import create_check_list, get_list_of_check

load_dotenv()


idx = 3

def main():
    # Получение токена для дальнейшей работы
    authorize = super_tocken()

    if authorize != 'Error':
        token = authorize
    else:
        exit(1)


    # Получение списка всех студентов
    get_all_students(base_url=base_url,
                     token=token)

    # Регистрация студентов
    register_students(base_url=base_url,
                      token=token,
                      email=f'student{idx}',
                      firstname=f'student{idx}',
                      lastname=f'studentov{idx}',
                      surname=f'studentovich{idx}',
                      birthday=f'2020-0{idx}-')

    print("Создание space")
    create_space(base_url=base_url,
                token=super_tocken(),
                name=f"space_{idx}")
    
    print("Создание занятия")
    # Создание занятия
    create_lesson(base_url=base_url,
                  token=token,
                  space_id=idx)

    # Получение токена для дальнейшей работы
    authorize = treiner_tocken()
    
    if authorize != 'Error':
        token = authorize
    else:
        exit(1)

    # Получение всех занятий
    print("Получение всех занятий")
    get_all_lessons(base_url=base_url,
                    token=token)
    
    # print("Создание check")
    # create_check_list(
    #     base_url=base_url,
    #     token=token)

    print("Получение всех check для тренера")
    # Получение всех check для тренера
    get_all_check(base_url=base_url,
                      token=token)
    
    print("Получение всех check для супера")
    # Получение всех check для супера
    get_all_check(base_url=base_url,
                      token=super_tocken())

if __name__ == "__main__":
    main()
