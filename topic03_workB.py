"""
B. Быстрый поиск в массиве
ограничение по времени на тест1 секунда
ограничение по памяти на тест512 мегабайт
вводстандартный ввод
выводстандартный вывод
Дан массив из 𝑛 целых чисел. Все числа от −109 до 109.

Нужно уметь отвечать на запросы вида «Cколько чисел имеют значения от 𝑙 до 𝑟»?

Входные данные
Число 𝑛 (1≤𝑛≤105). Далее 𝑛 целых чисел.

Затем число запросов 𝑘 (1≤𝑘≤105).

Далее 𝑘 пар чисел 𝑙,𝑟 (−109≤𝑙≤𝑟≤109) — собственно запросы.

Выходные данные
Выведите 𝑘 чисел — ответы на запросы.

Пример
входные данныеСкопировать
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2
выходные данныеСкопировать
5 2 2 0 

"""

from queue import Queue
import sys
 
MIN_VALUE = -10_000_000_000
MAX_VALUE = 10_000_000_000
 
 
def lower_bound(array, query):
    beg = -1
    end = len(array)
    while beg < end - 1:
        mid = (beg + end) // 2
        if query <= array[mid]:
            end = mid
        else:
            beg = mid
    return end
 
def upper_bound(array, query):
    return lower_bound(array, query + 1)
 
def count_elements_in_range(array, min_value, max_value):
    if min_value <= MIN_VALUE and max_value >= MAX_VALUE:
        return len(array)
 
    if min_value <= MIN_VALUE:
        left = 0
    else:
        left = lower_bound(array, min_value)
 
    if max_value >= MAX_VALUE:
        right = len(array)
    else:
        right = upper_bound(array, max_value)
    
    return max(0, right - left)
 
 
def naive_solution(array, min_value, max_value):
 
    def lower_bound(array, query):
        beg = 0
        end = len(array)
        while beg < end:
            mid = beg + (end - beg) // 2
            if array[mid] < query:
                beg = mid + 1
            else:
                end = mid
        return beg
 
    def upper_bound(array, query):
        beg = 0
        end = len(array)
        while beg < end:
            mid = beg + (end - beg) // 2
            if query < array[mid]:
                end = mid
            else:
                beg = mid + 1
        return beg
 
    if min_value <= MIN_VALUE and max_value >= MAX_VALUE:
        return len(array)
 
    if min_value <= MIN_VALUE:
        lb = 0
    else:
        lb = lower_bound(array, min_value)
 
    if max_value >= MAX_VALUE:
        ub = len(array)
    else:
        ub = upper_bound(array, max_value)
 
    result = max(0, ub - lb)
    return result
 
 
def cli_dialog():
    _ = int(sys.stdin.readline())
    arr = [int(x) for x in sys.stdin.readline().split()]
    k = int(sys.stdin.readline())
    queries = []
    for _ in range(k):
        l, r = [int(x) for x in sys.stdin.readline().split()]
        queries.append((l, r))
    arr.sort()
    results = []
    for l, r in queries:
        result = count_elements_in_range(
            array=arr,
            min_value=l,
            max_value=r
        )
        results.append(str(result))
    sys.stdout.write(" ".join(results) + "\n")
 
 
if __name__ == "__main__":
    cli_dialog()