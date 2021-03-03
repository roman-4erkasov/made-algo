"""
C. Остовное дерево
ограничение по времени на тест4 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Даны точки на плоскости, являющиеся вершинами полного графа. Вес ребра равен расстоянию между точками, соответствующими концам этого ребра. Требуется в этом графе найти остовное дерево минимального веса.

Входные данные
Первая строка входного файла содержит натуральное число 𝑛 — количество вершин графа (1≤𝑛≤10000). Каждая из следующих 𝑛 строк содержит два целых числа 𝑥𝑖, 𝑦𝑖  — координаты 𝑖-й вершины (−10000≤𝑥𝑖,𝑦𝑖≤10000). Никакие две точки не совпадают.

Выходные данные
Первая строка выходного файла должна содержать одно вещественное число — вес минимального остовного дерева.

Пример
входные данныеСкопировать
2
0 0
1 1
выходные данныеСкопировать
1.4142135624

"""

from math import sqrt
 
 
def dist(left, right):
    return sqrt(
        (right[0] - left[0]) ** 2 + (right[1] - left[1]) ** 2
    )
 
 
def prims_alg(nodes: list):
    INF = (10_000 - (-10_000)) ** 2 + (10_000 - (-10_000)) ** 2
    INVALID_RESULT = -1
    EMPTY_EDGE_END = -1
 
    n_nodes = len(nodes)
    result = 0
    used = [False for _ in range(n_nodes)]
    min_e = [INF for _ in range(n_nodes)]
    sel_e = [-1 for _ in range(n_nodes)]
    min_e[0] = 0
    for i in range(n_nodes):
        v = EMPTY_EDGE_END
        for j in range(n_nodes):
            if (not used[j]) and (v == EMPTY_EDGE_END or min_e[j] < min_e[v]):
                v = j
        if min_e[v] == INF:
            return INVALID_RESULT
        used[v] = True
        if sel_e[v] != EMPTY_EDGE_END:
            result += dist(nodes[v], nodes[sel_e[v]])
 
        for to in range(n_nodes):
            if v != to:
                d = dist(nodes[v], nodes[to])
                if d < min_e[to]:
                    min_e[to] = d
                    sel_e[to] = v
                    sel_e[v] = to
    return result
 
 
if __name__ == '__main__':
    n_nodes = int(input())
    nodes = []
    for _ in range(n_nodes):
        point = tuple([int(x) for x in input().split()])
        nodes.append(point)
    print(prims_alg(nodes))