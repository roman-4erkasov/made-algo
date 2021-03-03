"""
D. Остовное дерево 2
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Требуется найти в связном графе остовное дерево минимального веса.

Входные данные
Первая строка входного файла содержит два натуральных числа 𝑛 и 𝑚 — количество вершин и ребер графа соответственно. Следующие 𝑚 строк содержат описание ребер по одному на строке. Ребро номер 𝑖 описывается тремя натуральными числами 𝑏𝑖, 𝑒𝑖 и 𝑤𝑖 — номера концов ребра и его вес соответственно (1≤𝑏𝑖,𝑒𝑖≤𝑛, 0≤𝑤𝑖≤100000). 𝑛≤200000,𝑚≤200000.
Граф является связным.

Выходные данные
Первая строка выходного файла должна содержать одно натуральное число — вес минимального остовного дерева.

Пример
входные данныеСкопировать
4 4
1 2 1
2 3 2
3 4 5
4 1 4
выходные данныеСкопировать
7

"""

from sys import setrecursionlimit, stdin
import threading
 
 
def init(n: int):
    parent = []
    rank = []
    for i in range(n):
        parent.append(i)
        rank.append(0)
    return parent, rank
 
 
def get(
        idx: int, parent: list,
):
    if parent[idx] != idx:
        parent[idx] = get(parent[idx], parent)
    p_idx = parent[idx]
    return p_idx
 
 
def union(
        left: int, right: int,
        parent: list, rank: list,
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
    parent[left] = right
 
 
def kruskal(edges: list, n_nodes: int):
    result = 0
    edges = sorted(edges, key=lambda x: x[0])
    group, rank = init(n_nodes)
    for edge in edges:
        if get(idx=edge[1], parent=group) != get(idx=edge[2], parent=group):
            result += edge[0]
            union(left=edge[1], right=edge[2], parent=group, rank=rank)
    return result
 
 
def main():
    edges = []
    n_nodes, n_edges = [int(x) for x in input().split()]
    for _ in range(n_edges):
        beg, end, weight = [int(x) for x in input().split()]
        edges.append((weight, beg - 1, end - 1))
    print(kruskal(edges, n_nodes))
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()