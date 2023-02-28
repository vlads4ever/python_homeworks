""" Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами
элементы множеств."""

n = int(input('Введите n: '))
m = int(input('Введите m: '))

first_list = list()
second_list = list()

print('Введите элементы первого набора:')
for i in range(n):
    first_list.append(int(input(f'{i + 1}-е число: ')))

print('\nВведите элементы второго набора:')
for i in range(m):
    second_list.append(int(input(f'{i + 1}-е число: ')))

first_mult = set(first_list)
second_mult = set(second_list)

multiplicity = first_mult.union(second_mult)

result_list = list(multiplicity)
result_list.sort()

print(result_list)
