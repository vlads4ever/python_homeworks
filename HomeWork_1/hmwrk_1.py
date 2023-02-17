""" Задача 2: Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """

number = abs(int(input('Введите целое число: ')))
result = 0
flag = True

while flag:
    if number >= 10:
        result += number % 10
        number //= 10
    else:
        result += number
        flag = False

print(result)