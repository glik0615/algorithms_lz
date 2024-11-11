from random import randint

def main():
    list_1 = list()
    for i in range (100):
        list_1.append(randint(0,1000000))

    n = len(list_1)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_1[j] < list_1[j + 1]:
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]

    print(list_1)

from random import randint

def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
main() 