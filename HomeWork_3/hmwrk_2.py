""" Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X.
5
1 2 3 4 5
6
-> 5 """
from random import randint

n = int(input())

array = list()
for i in range(n):
    array.append(randint(-9, 9))
    print(f'{array[i]} ', end = '')

print()
x = int(input())

if x > array[0]:
    diff = x - array[0]
else:
    diff = array[0] - x

diff_index = 0

for i in range(1, n):
    if x > array[i]:
        current_diff = x - array[i]
    else:
        current_diff = array[i] - x
    
    if current_diff < diff:
        diff = current_diff
        diff_index = i
    
print(array[diff_index])