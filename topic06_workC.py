"""
C. Наибольшая возрастающая подпоследовательность
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Пусть a1, a2, ..., an — числовая последовательность. Длина последовательности — это количество элементов этой последовательности. Последовательность ai1, ai2, ..., aik называется подпоследовательностью последовательности a, если 1 ≤ i1 < i2 < ... < ik ≤ n. Последовательность a называется возрастающей, если a1 < a2 < ... < an.

Вам дана последовательность, содержащая n целых чисел. Найдите ее самую длинную возрастающую подпоследовательность.

Входные данные
В первой строке задано одно число n (1 ≤ n ≤ 2000) — длина подпоследовательности. В следующей строке задано n целых чисел ai ( - 109 ≤ ai ≤ 109) — элементы последовательности.

Выходные данные
В первой строке выведите число k — длину наибольшей возрастающей подпоследовательности. В следующей строке выведите k чисел — саму подпоследовательность.

Примеры
входные данныеСкопировать
8
1 4 1 5 3 3 4 2
выходные данныеСкопировать
3
1 4 5 
входные данныеСкопировать
3
1 2 3
выходные данныеСкопировать
3
1 2 3 

"""

from queue import deque
 
 
def LIS(arr):
    n = len(arr)
    d = [None for _ in range(n)]
    prev = [None for _ in range(n)]
    for i in range(n):
        d[i] = 1
        for j in range(i):
            if arr[j] < arr[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j
 
    # max length extraction
    id_max = None
    for i in range(n):
        if id_max is None or d[id_max] < d[i]:
            id_max = i
 
    # restoring subsequence
    seq = deque()
    curr = id_max
    while curr is not None:
        seq.appendleft(arr[curr])
        curr = prev[curr]
    return d[id_max], seq
 
 
def cli_dialog():
    _ = input()
    a = [int(x) for x in input().split()]
    length, subseq = LIS(a)
    print(length)
    print(" ".join([str(x) for x in subseq]))
 
 
if __name__ == "__main__":
    cli_dialog()