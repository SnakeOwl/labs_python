#!/usr/bin/python3

string = input("Введите строку для обработки: ")
result = []

latin = set('abcdefghijklmnopqrstuvwxyz')
russian_vowels = set ('аоэеиыуёюя')
digit = set('1234567890')

counter = 0;

for c in string:
    if c in digit:
        result.append('*')
    elif c in latin:
        result.append(c)
        counter += 1
    elif c in russian_vowels:
        result.append(c)
        result.append(c)
    else:
        result.append(c)

print('Исходные данные:')
print(string)
print('Количество прописных букв латинского алфавита: {0}'.format(counter))
print('Данные, полученные в результате обработки:')
print(''.join(result))
# Каждый день я пью water H2O
