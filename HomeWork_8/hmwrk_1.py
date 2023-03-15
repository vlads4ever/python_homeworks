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
    print('"exit" - для выхода из программы.')
    print('"help" - для отображения справки по командам.')
    print('"add ФИО телефон" - для добавления новой записи.')
    print('"show" - для вывода всех записей.')
    print('"find Фамилию или Имя" - для вывода указанной записи.')
    print('"change Фамилию или Имя" - для изменения указанной записи.')
    print('"delete Фамилию или Имя" - для удаления указанной записи.')


def add_new_rec(u_input: tuple) -> str:
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(';'.join(u_input) + '\n')
    return 'Запись добавлена'


def show_rec() -> str:
    with open('file.txt', 'r', encoding='utf-8') as file:
        return file.read().replace(';', ' ')


def find_rec(user_search: str) -> list:
    result = list()
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if user_search.lower() in line.lower():
                result.append(line.replace(';', ' ').rstrip())
    return result


def delete_rec(user_delete: str) -> str:
    find_list = find_rec(user_delete)
    if len(find_list) == 0:
        return 'Запись не найдена.'
    else:
        print('Найдены записи: ')
        print_list(find_list)

        with open('file.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        temp_data = ''
        for line in lines:
            if user_delete.lower() not in line.lower():
                temp_data += line
            else:
                print(f"Текущая запись: {line.replace(';', ' ')}")
                u_inp = input('Подтвердите удаление (y/n) > ')
                if u_inp.lower() == 'n':
                    temp_data += line
                    message = 'Запись не была удалена.'
                else:
                    message = 'Запись удалена.'

        with open('file.txt', 'w', encoding='utf-8') as file:
            file.write(temp_data)

        return message


def change_rec(user_change: str) -> str:
    find_list = find_rec(user_change)
    if len(find_list) == 0:
        return 'Запись не найдена.'
    else:
        print('Найдены записи: ')
        print_list(find_list)

        with open('file.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

            temp_data = ''
            for line in lines:
                if user_change.lower() not in line.lower():
                    temp_data += line
                else:
                    print(f"Текущая запись: {line.replace(';', ' ')}")
                    print(
                        'Введите изменения или Enter - оставить без изменений:'
                        )
                    u_inp = tuple(input('New Record > ').split())
                    if len(u_inp) == 0:
                        temp_data += line
                        message = 'Запись оставлена без изменений'
                    else:
                        temp_data += ';'.join(u_inp) + '\n'
                        message = 'Запись изменена.'

            with open('file.txt', 'w', encoding='utf-8') as file:
                file.write(temp_data)

            return message


def print_list(user_list):
    for i in user_list:
        print(i)


print_help()

while True:
    user_input = input('Phone Book > ')
    tuple_input = tuple(user_input.split())
    if tuple_input[0] == 'exit':
        break
    elif tuple_input[0] == 'help':
        print_help()
    elif tuple_input[0] == 'add':
        print(add_new_rec(tuple_input[1:]))
    elif tuple_input[0] == 'show':
        print(show_rec())
    elif tuple_input[0] == 'find':
        result = find_rec(tuple_input[1])
        if len(result) == 0:
            print('Запись не найдена.')
        else:
            print_list(result)
    elif tuple_input[0] == 'delete':
        print(delete_rec(tuple_input[1]))
    elif tuple_input[0] == 'change':
        print(change_rec(tuple_input[1]))
