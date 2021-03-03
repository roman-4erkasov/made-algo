"""
E. Простая сортировка
ограничение по времени на тест2 секунды
ограничение по памяти на тест64 мегабайта
вводстандартный ввод
выводстандартный вывод
Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания.

Входные данные
В первой строке входного файла содержится число N (1 ≤ N ≤ 100 000) — количество элементов в массиве. Во второй строке находятся N целых чисел, по модулю не превосходящих 109.

Выходные данные
В выходной файл надо вывести этот же массив в порядке неубывания, между любыми двумя числами должен стоять ровно один пробел.

Пример
входные данныеСкопировать
10
1 8 2 1 4 7 3 2 3 6
выходные данныеСкопировать
1 1 2 2 3 3 4 6 7 8 
Примечание
Запрещается использовать стандартные сортировки.
"""


import random
from queue import Queue
 
 
def partition_3(array, head, tail):
    idx_random = random.randint(head, tail)
    if head <= idx_random <= tail or tail <= idx_random <= head:
        array[tail], array[idx_random] = array[idx_random], array[tail]
    elif head <= tail <= idx_random or idx_random <= tail <= head:
        array[tail], array[head] = array[head], array[tail]
    pivot = array[tail]
    before_border = head - 1
    after_border = tail + 1
    idx_check = head
    while idx_check < after_border:
        if array[idx_check] < pivot:
            before_border += 1
            array[idx_check], array[before_border] = array[before_border], array[idx_check]
            idx_check += 1
        elif pivot < array[idx_check]:
            after_border -= 1
            array[idx_check], array[after_border] = array[after_border], array[idx_check]
        else:
            idx_check += 1
    return before_border, after_border
 
 
def quicksort_3(array):
    que = Queue()
    que.put((0, len(array) - 1))
    while not que.empty():
        head, tail = que.get()
        if head < tail:
            tail_left, head_right = partition_3(array, head, tail)
            que.put((head, tail_left))
            que.put((head_right, tail))
 
 
if __name__ == '__main__':
    _ = int(input())
    array = [int(x) for x in input().split()]
    quicksort_3(array)
    print(" ".join([str(x) for x in array]))