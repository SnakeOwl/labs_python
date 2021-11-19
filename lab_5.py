f_in = open('input.txt', 'r')
f_out = open('output.txt', 'w')
new_dict = dict()

# В цикле нужно заморочится с синонимами, поэтому такой большой и не понятный
for line in f_in:
    split_line = line.split(' - ', 1)
    # сейчас в split_line содержится массив из 2-х строк.
    # первая строка английский перевод, вторая русский

    if split_line[0] == '\n': # После считывания всех строк, будут пустые строки, их пропустить.
        break

    split_line[1] = split_line[1].rstrip() # обрезка символа '\n'

    # разбивка синонимов
    try:
        eng_part = [ split_line[0] ]
        rus_part = split_line[1]
        split_sinonyms = rus_part.split(', ')

        for rus_word in split_sinonyms:
            eng_part_t = new_dict.get(rus_word, 1) # вернет список list
            if eng_part_t != 1:
                eng_part_t.append (split_line[0])
                new_dict.update ({ rus_word : eng_part_t })
            else:
                new_dict.update ({ rus_word : eng_part })

    except IndexError: # Когда рзаделяешь строку, а в строке указанного разделителя нет.
        eng_part_t = new_dict.get ( rus_part, 1 )
        if eng_part_t != 1:
            eng_part_t.append(eng_part)
            new_dict.update ({ rus_part :  eng_part_t})
        else:
            new_dict.update ({ rus_part : eng_part })


# сортировка по первому ключу (там у меня русский перевод)
sorted_dict = dict (sorted (new_dict.items(), key=lambda item: item[0] ) )

for key in sorted_dict:
    line = key + ' - '
    list = sorted_dict[key]
    for object in list:
        line += object + ", "

    line = line[:-2] #синтаксис обрезки символов в конце
    line += '\n'
    f_out.write(line)

f_out.close()
