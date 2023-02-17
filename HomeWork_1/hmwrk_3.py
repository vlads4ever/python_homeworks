""" Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no """

ticket_number = int(input('Введите шестизначный номер билета: '))

# Первый вариант

first_sum = 0
second_sum = 0
first_half = 0

if ticket_number >= 100000 and ticket_number <= 999999:
    text_number = str(ticket_number)
    for symbol in text_number:
        digit = int(symbol)
        if first_half < 3: 
            first_sum += digit
            first_half += 1
        else:
            second_sum += digit

    if first_sum == second_sum:
        print('yes')
    else:
        print('no')
else:
    print('Такого номера не может быть')

############################################################

# Второй вариант

first_sum = 0
second_sum = 0
first_half = 0
flag = True

if ticket_number >= 100000 and ticket_number <= 999999:
    while flag:        
        if ticket_number >= 10:            
            if first_half < 3:
                first_sum += ticket_number % 10
                ticket_number //= 10
                first_half += 1
            else:
                second_sum += ticket_number % 10
                ticket_number //= 10
        else:
            second_sum += ticket_number
            flag = False

    if first_sum == second_sum:
        print('yes')
    else:
        print('no')
else:
    print('Такого номера не может быть')