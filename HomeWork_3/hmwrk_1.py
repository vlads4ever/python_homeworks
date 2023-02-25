""" Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X.
5
1 2 3 4 5
3
-> 1 """

from random import randint

n = int(input('Введите N: '))

array = list()
for i in range(n):
    array.append(randint(0, 9))
    print(f'{array[i]} ', end='')

print()
x = int(input('Введите X: '))

# Вариант с методом count()
count = array.count(x)
print(count)

# Вариант с циклом
count = 0
for i in range(n):
    if x == array[i]:
        count += 1

print(count)
