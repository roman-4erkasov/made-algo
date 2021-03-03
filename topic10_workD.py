"""
D. Конденсация графа
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Конденсацией графа 𝐺 называется новый граф 𝐻, где каждой компоненте сильной связности в графе 𝐺 соответствует вершина из графа 𝐻. Ребро 𝑣𝑢 в графе 𝐻 есть тогда и только тогда, когда в графе 𝐺 существует хотя бы одно ребро из соответствующей 𝑣 компоненте сильной связности, в компоненту, соответствующую 𝑢.

Требуется найти количество ребер в конденсации ориентированного графа.

Примечание: конденсация графа не содержит кратных ребер.

Входные данные
Первая строка входного файла содержит два натуральных числа 𝑛 и 𝑚 — количество вершин и ребер графа соответственно (𝑛≤10000, 𝑚≤100000). Следующие 𝑚 строк содержат описание ребер, по одному на строке. Ребро номер 𝑖 описывается двумя натуральными числами 𝑏𝑖, 𝑒𝑖 — началом и концом ребра соответственно (1 ≤ 𝑏𝑖, 𝑒𝑖 ≤ 𝑛). В графе могут присутствовать кратные ребра и петли.

Выходные данные
Единственная строка выходного файла должна содержать одно число — количество ребер в конденсации графа.

Пример
входные данныеСкопировать
4 4
2 1
3 2
2 3
4 3
выходные данныеСкопировать
2

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
 
    WHITE = 0
    GRAY = 1
    BLACK = 2
    colors = [WHITE for _ in range(n_nodes)]
 
    def dfs(node_src: int, passed):
        seen.add(node_src)
        colors[node_src - 1] = GRAY
        for node_trg in graph[node_src]:
            if colors[node_trg - 1] == WHITE:
                dfs(node_trg, passed)
        colors[node_src - 1] = BLACK
        result.appendleft(node_src)
 
    for node in range(1, n_nodes + 1):
        if node not in seen:
            passed_in_traverse = set()
            dfs(node, passed_in_traverse)
    return result
 
 
def find_cc(graph: defaultdict, nodes):
    NO_COLOR = 0
    n_nodes = len(nodes)
    colors = [NO_COLOR for _ in range(n_nodes)]
 
    def dfs(node_src: int, curr: int):
        colors[node_src - 1] = curr
        for node_trg in graph[node_src]:
            if colors[node_trg - 1] == NO_COLOR:
                dfs(node_trg, curr)
 
    count = 0
    for node in nodes:
        if colors[node - 1] == NO_COLOR:
            count += 1
            dfs(node, count)
    return colors
 
 
def count_edges(graph: defaultdict, rgraph: defaultdict, n_nodes: int, edges: set):
    nodes = topological_sort(graph, n_nodes)
    colors = find_cc(rgraph, nodes)
    condensated_edges = set()
    for node1, node2 in edges:
        if colors[node1 - 1] != colors[node2 - 1]:
            condensated_edges.add(
                (colors[node1 - 1], colors[node2 - 1])
            )
    return len(condensated_edges)
 
 
def main():
    graph = defaultdict(list)
    rgraph = defaultdict(list)
    edges = set()
    n_nodes, n_edges = [int(x) for x in input().split()]
    for _ in range(n_edges):
        node1, node2 = [int(x) for x in input().split()]
        graph[node1].append(node2)
        rgraph[node2].append(node1)
        edges.add((node1, node2))
    print(count_edges(graph=graph, rgraph=rgraph, n_nodes=n_nodes, edges=edges))
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()