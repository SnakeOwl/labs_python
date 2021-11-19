#!/usr/bin/python3

def main (list):
    min = my_list[0];# берем первое значение, оно же будет первым при сравнении
    counter = 0;     # поэтому counter = 0

    for i in my_list:
        if min == i:
            counter += 1;
        elif min > i:
            min = i;
            counter = 1;

    print("Список:");
    print(my_list);
    print("Минимальное значение: {0}, количество одинаковых с ним элементов: {1}".format(min, counter));


my_list = [1,2,3,4,1,23,4];
main (my_list)


