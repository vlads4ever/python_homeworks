# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


def get_arithmetic_progression(param: list[int]) -> list[int]:
    output_list = list()
    first_el = param[0]
    diff = param[1]
    count = param[2]
    for i in range(count):
        output_list.append(first_el + i * diff)
    return output_list


user_input = list(map(int, input(
    'Введите первый элемент, разность и колличество: ').split()))
print(*get_arithmetic_progression(user_input))
