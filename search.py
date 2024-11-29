import random
from random import randint as ri
list_1 = random.sample(range(1000001), 100)
# sample - выбирает случайные элементы из указанного диапазона без дубликатов

print('Список 2')
list_2 = random.sample(range(1000001), 100)
list_2.sort()
print(list_2)

l = int(input('искомый элемент:'))
# l - элемент
m = 0 
# m = количество сравнений
if l in list_1: # если элемент находится в list_1
    for i in range(0, len(list_1)):
        m = m + 1 # прибавляем каждый цикл +1
        if list_1[i] == l:
            break 
    print(f'Индекс искомого элемента из первого списка:{i}')
    print(f'Количество сравнений в линейном поиске:{m}')
else:
    print("Элемент не найден в первом списке")

# Бинарный поиск
if l in list_2: # есть ли элемент в списке
    first = 0
    last = len(list_2)-1
    m_2 = 0
    k = 1 # k - индекс
    while (first <= last) and k == 1:
        mid = (first+last)//2 # индекс элемента в середине списка
        m_2 = m_2 + 1 #прибавляем каждый цикл +1
        if list_2[mid] == l:
            k = mid
        else: 
            if l<list_2[mid]:
                last = mid -1
            else:
                first = mid +1
    print(f'Количество сравнений в бинарном поиске:{m_2}')
    print(f'Индекс искомого элементата из второго списка:{k}')
else:
    print("Элемент не найден во втором списке")