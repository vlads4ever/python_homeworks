""" Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 """


def my_pow(a: int, b: int) -> int:
    if (a == 0 and b == 0) or a == 1:
        return 1
    elif b == 1:
        return a
    else:
        return a * my_pow(a, b - 1)


a = int(input('Введите A: '))
b = int(input('Введите B: '))

print(my_pow(a, b))
