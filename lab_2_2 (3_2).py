#!/usr/bin/python3
from goto import with_goto

# ===== my functions =====
def is_number_even(n):
    if n % 2 == 0:
        return 1
    else :
        return 0
    

# ===== main stack ======
can_continue_1 = 1
while (can_continue_1):
    try:
        n = int (input ("Введите количество элементов: ") )
        can_continue_1 = 0
    except Exception:
        print("Не могу считать число, пожалуйста введите снова.")


my_list = []
i = 0
while (i < n):
    i += 1
    can_continue_2 = 1
    while (can_continue_2):
        try:
            my_list.append (int (input ("Введите число: ") ) )
            can_continue_2 = 0
        except Exception:
            print("Не могу считать число, пожалуйста введите снова.")

max = 0
counter = 0

for i in my_list:
    if is_number_even(i) :
        counter += 1
    elif max < i :
        max = i

print("Список:")
print(my_list)

if max == 0 :
    print("В списке нет нечетных чисел.")
else :
    print("Максимальное нечетное значение: {0}".format(max))

print("Количество четных чисел: {0}".format(counter))
