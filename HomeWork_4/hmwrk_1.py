""" Задача 22: Даны два неупорядоченных набора целых чисел
(может быть, с повторениями). Выдать без повторений в порядке
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 списка. 1 строка - первый список через
пробел. 2 строка - второй список через пробел."""

first_list = list(map(int, input('Введите первый набор: ').split()))
second_list = list(map(int, input('Введите второй набор: ').split()))

first_mult = set(first_list)
second_mult = set(second_list)

multiplicity = first_mult.union(second_mult)

result_list = list(multiplicity)
result_list.sort()

print(*result_list)
