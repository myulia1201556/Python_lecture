# Дан список чисел. Создайте список, в который попадают числа,
#  описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:* 
#  [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


import random

list = [x for x in range(1, 10)]
random.shuffle(list)
print(list)

list_of_list = []
for i in range(len(list) - 1):
    under_list = [list[i]]
    for k in range(i, len(list) - 1):
        if list[k] < list[k + 1]:
            under_list.append(list[k + 1])
        else:
                break
    if len(under_list) > 1 and "".join(map(str, under_list)) not in ["".join(map(str, i)) for i in list_of_list]:
        list_of_list.append(under_list)
print(list_of_list)