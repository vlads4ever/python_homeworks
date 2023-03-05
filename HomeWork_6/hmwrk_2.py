# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint as rnd


def get_range_index(
        arr: list[int], lower_lim: int, upper_lim: int) -> list[int]:
    output_list = list()
    for i in range(len(arr)):
        if lower_lim <= arr[i] <= upper_lim:
            output_list.append(i)
    return output_list


def get_random_list(count: int, lower_lim: int, upper_lim: int) -> list[int]:
    output_list = list()
    for i in range(count):
        output_list.append(rnd(lower_lim, upper_lim))
    return output_list


user_input = list(map(int, input(
    'Введите длину, диапазон значений массива и диапазон поиска: ').split()))
rand_list = get_random_list(user_input[0], user_input[1], user_input[2])
print(rand_list)
print(get_range_index(rand_list, user_input[3], user_input[4]))
