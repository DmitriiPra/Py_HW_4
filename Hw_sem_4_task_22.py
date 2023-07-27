"""
Задача 22
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
"""
import random

arr1 = int(input("введите количество чисел в первом наборе: "))
arr2 = int(input("введите количество чисел во втором наборе: "))

if arr1 > 0 and arr2 > 0:
    arr_num_1 = []
    arr_num_2 = []
    for i in range(arr1):
        arr_num_1.append(random.randint(-9, 9))
    print(arr_num_1)
    for i in range(arr2):
        arr_num_2.append(random.randint(-9, 9))
    print(arr_num_2)

    intersect_arr = set(arr_num_1).intersection(set(arr_num_2))
    result = list(intersect_arr)
    result.sort()
    print()
    print(*result)
else:
    print("введите значения больше нуля!")
