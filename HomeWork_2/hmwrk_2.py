""" Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3 """

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

s = correct_natural_number('Введите сумму S: ')
p = correct_natural_number('Введите произведение P: ')

discriminant = s ** 2  - 4 * p

if discriminant > 0:
    x = (s - discriminant ** 0.5) / 2   
    y = s - x
    if x == int(x) and y == int(y):
        print (f'{x} и {y}')
    else:
        print('Таких натуральных чисел быть не может')
elif discriminant == 0:
    x = s / 2
    y = s - x
    print (f'{x} и {y}')
else:
    print('Таких чисел быть не может')
