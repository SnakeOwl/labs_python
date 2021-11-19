#!/usr/bin/python3

# по факту: считать текст, найти минимальное по длине слово, заменить во всех словах первую букву на букву минимального слова
    
origin_string = input("Введите предложение для обработки: ")

words = origin_string.split(' ') #разбиваю предложение по словам
min = len(words[0])
min_word = words[0]
min_first_char = words[0][0] #нужен первый символ для замены

#поиск минимального по длине слова
for word in words:
    if word == '-':
        continue

    lenght = len(word)
    
#на конце слова могут быть знаки препинания
    if word.endswith(',', 2) or word.endswith('.', 2) or word.endswith(':', 2): 
        lenght -= 1

    if lenght < min:
        min = lenght
        min_first_char = word[0]
        min_word = word

result = []
# минимальное по длине слово найдено, теперь нужно произвести замену
for word in words:
    result.append(word.replace(word[0], min_first_char, 1)) #заменяю первый символ в слове 

print ('Минимальное по длине слово: {0}'.format(min_word))
print ('Полученное предложение: {0}'.format(' '.join(result)))


    

    

    
        
    

    


