"""
A. Компоненты связности
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Дан неориентированный граф. Требуется выделить компоненты связности в нем.

Входные данные
Первая строка входного файла содержит два натуральных числа 𝑛 и 𝑚 — количество вершин и ребер графа соответственно (1≤𝑛≤100000, 0≤𝑚≤200000).

Следующие 𝑚 строк содержат описание ребер по одному на строке. Ребро номер 𝑖 описывается двумя натуральными числами 𝑏𝑖, 𝑒𝑖 — номерами концов ребра (1≤𝑏𝑖,𝑒𝑖≤𝑛). Допускаются петли и параллельные ребра.

Выходные данные
В первой строке выходного файла выведите целое число 𝑘 — количество компонент связности графа. Во второй строке выведите 𝑛 натуральных чисел 𝑎1,𝑎1,…,𝑎𝑛, не превосходящих 𝑘, где 𝑎𝑖 — номер компоненты связности, которой принадлежит 𝑖-я вершина.

Примеры
входные данныеСкопировать
3 1
1 2
выходные данныеСкопировать
2
1 1 2
входные данныеСкопировать
4 2
1 3
2 4
выходные данныеСкопировать
2
1 2 1 2

"""

from sys import setrecursionlimit
import threading
 
 
def count_connected_components(graph: list):
    NO_COLOR = 0
 
    def dfs_rec(node, color_curr):
        colors[node] = color_curr
        for node_trg in graph[node]:
            if colors[node_trg] == NO_COLOR:
                dfs_rec(node_trg, color_curr)
 
    n_nodes = len(graph)
    count = 0
    colors = [NO_COLOR for _ in range(n_nodes)]
    for node in range(n_nodes):
        if colors[node] == NO_COLOR:
            count += 1
            dfs_rec(node, count)
    return count, colors
 
 
def main():
    n_nodes, n_edges = [int(x) for x in input().split()]
 
    graph = [set() for _ in range(n_nodes)]
 
    for _ in range(n_edges):
        v_src, v_trg = [int(x) for x in input().split()]
        graph[v_src - 1].add(v_trg - 1)
        graph[v_trg - 1].add(v_src - 1)
 
    n_colors, colors = count_connected_components(graph)
    print(n_colors)
    print(" ".join([str(x) for x in colors]))
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()