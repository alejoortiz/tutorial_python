def my_division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0


result = my_division(10, 0)


def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('el archivo no se encuentra')


result = read_file('.txt')

import traceback

def check_name_in_people(people):
    try:
        name = people['name']
        return name
    except Exception as error:
        print(error.__doc__)
        print(traceback.format_exc())


people = {
    'age': 30,
    'zip': 110089
    }

result = check_name_in_people(people)
