# Задача No49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Задача 38: Дополнить телефонный справочник
# возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал
# для изменения и удаления данных.


def print_help():
    print('"exit" - Выход из программы.')
    print('"help" - Отображение справки по командам.')
    print('"add ФИО телефон" - Добавление новой записи.')
    print('"show" - Вывод всех записей.')
    print('"find Фамилию или Имя" - Вывод указанной записи.')
    print('"change Фамилию или Имя" - Изменение указанной записи.')
    print('"delete Фамилию или Имя" - Удаление указанной записи.')


def add_new_rec(u_input: tuple) -> str:
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f"{u_input[1]};{u_input[2]};{u_input[3]};{u_input[4]}\n")
    return 'Запись добавлена'


def show_rec():
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(str(line.replace(';', ' ')))


def find_rec(user_search: str) -> str:
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if user_search.lower() in line.lower():
                return str(line.replace(';', ' '))
        return ('Запись отсутствует.')


def delete_rec(user_delete: str) -> str:
    message = 'Запись не обнаружена.'
    with open('file.txt', 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)  # Для записи с начала документа
        for line in lines:
            if user_delete.lower() not in line.lower():
                file.write(line)
            else:
                message = 'Запись удалена.'
        file.truncate()  # Усечение остатка файла с текущей позиции курсора
    return message


def change_rec(user_change: str) -> str:
    message = 'Запись не найдена.'
    with open('file.txt', 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if user_change.lower() not in line.lower():
                file.write(line)
            else:
                print(f"Найдена запись: {str(line.replace(';', ' '))}")
                print('Введите измененную строку:')
                u_inp = tuple(input('New Record > ').split())
                file.write(f"{u_inp[0]};{u_inp[1]};{u_inp[2]};{u_inp[3]}\n")
                message = 'Запись изменена.'
        file.truncate()
    return message


print_help()

while True:
    user_input = input('Phone Book > ')
    tuple_input = tuple(user_input.split())
    if tuple_input[0] == 'exit':
        break
    elif tuple_input[0] == 'help':
        print_help()
    elif tuple_input[0] == 'add':
        print(add_new_rec(tuple_input))
    elif tuple_input[0] == 'show':
        show_rec()
    elif tuple_input[0] == 'find':
        print(find_rec(tuple_input[1]))
    elif tuple_input[0] == 'delete':
        print(delete_rec(tuple_input[1]))
    elif tuple_input[0] == 'change':
        print(change_rec(tuple_input[1]))
