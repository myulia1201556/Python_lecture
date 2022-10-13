# Реализуйте алгоритм задания случайных чисел без использования встроенного 
# генератора псевдослучайных чисел.

import time

def rondom(min, max, n2):
    list = []
    num = 0
    maximum = 0
    if max <= 10:
        maximum = 10
    elif max <= 100:
        maximum = 100
    elif max <= 1000:
        maximum = 1000

    for i in range(1, n2+1):
        num = (round(i * (time.time() * 1000) % maximum))
        if min > num or num > max:
            while min > num or num > max:
                num = (round(i * (time.time() * 1000) % maximum))
        list.append(num)

    return list


list = rondom(10, 50, 8)
print(list)