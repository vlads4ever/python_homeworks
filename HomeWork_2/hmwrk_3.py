""" Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2^k), не превосходящие числа N.
10 -> 1 2 4 8 """

def correct_natural_number(message) -> int:    
    is_correct = True
    while is_correct:
        a = input(message)
        try:
            a = int(a)
            if a > 0:
                is_correct = False
                return a
            else:
                print('Не натуральное число')
        except ValueError:
            print('Некорректный ввод')

number = correct_natural_number('Введите натуральное число: ')

current_number = 2 ** 0

while current_number <= number:
    print(current_number, end=" ")
    current_number *= 2