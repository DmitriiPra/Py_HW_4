"""
Задача 24
черника растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет  N  кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
Cистема сбора состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном списке урожайности грядки.
"""
import random

amount_n = int(input("введите количество кустов на грядке: "))
result = 0
if amount_n > 2:
    berry_list = []
    for i in range(amount_n):
        berry_list.append(random.randint(10, 20))
    print(berry_list)
    count = 0
    for i in range(amount_n):
        if i == 0:
            count = berry_list[i] + berry_list[i + 1] + berry_list[amount_n - 1]
            if count > result:
                result = count
        elif i == amount_n - 1:
            count = berry_list[i] + berry_list[i - 1] + berry_list[0]
            if count > result:
                result = count
        else:
            count = berry_list[i] + berry_list[i + 1] + berry_list[i - 1]
            if count > result:
                result = count
    print(result)
else:
    print("введите количество кустов не менее 3")
