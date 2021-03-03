"""
C. Топологическая сортировка
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Дан ориентированный невзвешенный граф. Необходимо построить его топологическую сортирвоку.

Входные данные
В первой строке входного файла даны два натуральных числа 𝑛 и 𝑚 (1≤𝑛≤100000, 0≤𝑚≤100000) — число вершин и рёбер в графе соответственно. Далее в 𝑚 строках перечислены рёбра графа. Каждое ребро задаётся парой чисел — номерами начальной и конечной вершин соответственно.

Выходные данные
Выведите любую топологическую сортировку графа в виде последовательности номеров вершин. Если граф невозможно топологически отсортировать, выведите −1.

Пример
входные данныеСкопировать
6 6
1 2
3 2
4 2
2 5
6 5
4 6
выходные данныеСкопировать
4 6 3 1 2 5 

"""
from sys import setrecursionlimit
import threading
from collections import defaultdict, deque
 
 
def topological_sort(graph: defaultdict, n_nodes: int):
    """
    Topological sorting algorithm
    :param graph: graph as dict with lists of children nodes
    :param n_nodes: number of nodes in graph
    :return: nodes ordered in topological order
    """
    seen = set()
    result = deque()
    has_cycles = False
 
    WHITE = 0
    GRAY = 1
    BLACK = 2
    colors = [WHITE for _ in range(n_nodes)]
 
    def dfs(node_src: int, passed):
        nonlocal has_cycles
        seen.add(node_src)
        colors[node_src - 1] = GRAY
        for node_trg in graph[node_src]:
            if colors[node_trg - 1] == WHITE:
                dfs(node_trg, passed)
            if colors[node_trg - 1] == GRAY:
                has_cycles = True
                break
        colors[node_src - 1] = BLACK
        if not has_cycles:
            result.appendleft(node_src)
 
    for node in range(1, n_nodes + 1):
        if node not in seen:
            passed_in_traverse = set()
            dfs(node, passed_in_traverse)
    if has_cycles:
        return [-1]
    else:
        return result
 
 
def main():
    graph = defaultdict(list)
    n_nodes, n_edges = [int(x) for x in input().split()]
    for _ in range(n_edges):
        node_src, node_trg = [int(x) for x in input().split()]
        graph[node_src].append(node_trg)
    print(
        " ".join(
            map(str, topological_sort(graph=graph, n_nodes=n_nodes))
        )
    )
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()