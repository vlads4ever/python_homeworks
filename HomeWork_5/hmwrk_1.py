""" Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 """


def myPow(a: int, b: int) -> int:
    if b == 1:
        return a
    else:
        return a * myPow(a, b - 1)


a = int(input('Введите A: '))
b = int(input('Введите B: '))

print(myPow(a, b))
