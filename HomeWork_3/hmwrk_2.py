""" Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n)
самый близкий по величине элемент к заданному числу X. Пользователь в
первой строке вводит натуральное число N – количество элементов в массиве.
Последняя строка содержит число X
 *Пример:*
5
    1 2 3 4 5
    6
    -> 5 """

# Вариант для массива из натуральных чисел

n = int(input('Введите N: '))
array = [i for i in range(1, n + 1)]
print(array)
print()
x = int(input('Введите X: '))

diff = abs(array[0] - x)
nearest_index = 0

for i in range(1, len(array)):
    if abs(array[i] - x) < diff:
        diff = abs(array[i] - x)
        nearest_index = i

print(array[nearest_index])
