# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его
# стихах ритм. Поскольку разобраться в его кричалках не настолько
# просто, насколько легко он их придумывает, Вам стоит написать
# программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга
# пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
# “Пам парам”, если с ритмом все не в порядке.

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам

# Вывод:
# Парам пам-пам


# any_rhythm = lambda screamer, vowels: len(set(map(lambda phrase: len(
#    list(filter(lambda letter: letter in vowels, phrase))), list(
#       screamer.split())))) == 1
# if any_rhythm(screamer, vowels):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


def vowels_list(phrase):
    res = list(filter(lambda letter: letter.lower() in vowels, phrase))
    return res


screamer = 'пУра-ра-рам рем-пем-папам па-ра-па-дам'
vowels = {'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'}
phrase_list = list(screamer.split())
rhythm_set = set(map(lambda phrase: len(vowels_list(phrase)), phrase_list))
if len(rhythm_set) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
