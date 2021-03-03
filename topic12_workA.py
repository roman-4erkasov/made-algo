"""
A. Система непересекающихся множеств
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Реализуйте систему непересекающихся множеств. Вместе с каждым множеством храните минимальный, максимальный элемент в этом множестве и их количество.

Входные данные
Первая строка входного файла содержит n — количество элементов в носителе (1 ≤ n ≤ 300 000). Далее операций с множеством. Операция get должна возвращать минимальный, максимальный элемент в соответствующем множестве, а также их количество.

Выходные данные
Выведите последовательно результат выполнения всех операций get.

Пример
входные данныеСкопировать
5
union 1 2
get 3
get 2
union 2 3
get 2
union 1 3
get 5
union 4 5
get 5
union 4 1
get 5
выходные данныеСкопировать
3 3 1
1 2 2
1 3 3
5 5 1
4 5 2
1 5 5
"""

from sys import setrecursionlimit, stdin
import threading
 
 
def init(n: int):
    parent = []
    rank = []
    subset_size = []
    subset_min = []
    subset_max = []
    for i in range(n):
        parent.append(i)
        rank.append(0)
        subset_size.append(1)
        subset_min.append(i)
        subset_max.append(i)
    return parent, rank, subset_size, subset_min, subset_max
 
 
def get(
        idx: int, parent: list,
):
    if parent[idx] != idx:
        parent[idx] = get(parent[idx], parent)
    p_idx = parent[idx]
    return p_idx
 
 
def get_output(
        idx: int,
        parent: list,
        subset_size: list,
        subset_min: list,
        subset_max: list
):
    if parent[idx] != idx:
        parent[idx] = get(parent[idx], parent)
    p_idx = parent[idx]
    return subset_min[p_idx] + 1, subset_max[p_idx] + 1, subset_size[p_idx]
 
 
def union(
        left: int, right: int,
        parent: list, rank: list,
        subset_size: list, subset_min: list, subset_max: list
):
    left = get(
        idx=left,
        parent=parent,
    )
    right = get(
        idx=right,
        parent=parent,
    )
    if left == right:
        return
    if rank[left] > rank[right]:
        left, right = right, left
    if rank[left] == rank[right]:
        rank[right] += 1
    subset_size[right] += subset_size[left]
    subset_max[right] = max(
        subset_max[left],
        subset_max[right]
    )
    subset_min[right] = min(
        subset_min[left],
        subset_min[right]
    )
    parent[left] = right
 
 
def main():
    set_size = int(input())
    parent, rank, subset_size, subset_min, subset_max = \
        init(set_size)
    line: str = None  # for autocompletion in PyCharm
    for line in stdin:
        if line == '':
            break
        elif line.startswith("union"):
            command = line.split()
            union(
                left=int(command[1]) - 1,
                right=int(command[2]) - 1,
                parent=parent,
                rank=rank,
                subset_size=subset_size,
                subset_min=subset_min,
                subset_max=subset_max
            )
        elif line.startswith("get"):
            command = line.split()
            res = get_output(
                idx=int(command[1]) - 1,
                parent=parent,
                subset_size=subset_size,
                subset_min=subset_min,
                subset_max=subset_max
            )
            print(" ".join([str(x) for x in res]))
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()