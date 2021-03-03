"""
B. Репосты
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Однажды Поликарп опубликовал в социальной сети смешную картинку с опросом про цвет своего хэндла. Многие из его друзей стали репостить шутку Поликарпа себе в ленту. Некоторые из них репостили репосты и так далее.

Эти события заданы в виде последовательности строк «name1 reposted name2» где name1 — это имя того, кто репостнул, а name2 — имя того, с чей ленты репостнули шутку. Гарантируется, что для каждой строки «name1 reposted name2» пользователь «name1» еще не имел эту шутку в свой ленте, а «name2» уже имел ее в своей ленте к моменту репоста. Поликарп зарегистрирован под именем «Polycarp», и изначально шутка есть только в его ленте.

Поликарп измеряет успешность шутки как длину наибольшей цепочки репостов. Выведите успешность шутки Поликарпа.

Входные данные
В первой строке входных данных записано целое число n (1 ≤ n ≤ 200) — количество репостов. Далее записаны сами репосты в порядке их совершения. Каждый из них записан в отдельной строке и имеет вид «name1 reposted name2». Все имена во входных данных состоят из прописных или строчных латинских букв и/или цифр и имеют длины от 2 до 24 символов включительно.

Известно, что имена пользователей регистронезависимы, то есть два имени, отличающиеся исключительно регистром букв, соответствуют одному и тому же пользователю соцсети.

Выходные данные
Выведите единственное целое число — максимальную длину цепочки репостов.

Примеры
входные данныеСкопировать
5
tourist reposted Polycarp
Petr reposted Tourist
WJMZBMR reposted Petr
sdya reposted wjmzbmr
vepifanov reposted sdya
выходные данныеСкопировать
6
входные данныеСкопировать
6
Mike reposted Polycarp
Max reposted Polycarp
EveryOne reposted Polycarp
111 reposted Polycarp
VkCup reposted Polycarp
Codeforces reposted Polycarp
выходные данныеСкопировать
2
входные данныеСкопировать
1
SoMeStRaNgEgUe reposted PoLyCaRp
выходные данныеСкопировать
2
"""

from sys import setrecursionlimit
import threading
from collections import defaultdict
 
 
def main():
    def dfs(node1, node2):
        dist[node1] = 1
        for node_trg in graph[node1]:
            if node_trg != node2:
                dfs(node_trg, node1)
                dist[node1] = max(dist[node1], dist[node_trg] + 1)
 
    FIRST = "polycarp"
    dist = dict()
    n_queries = int(input())
    graph = defaultdict(list)
    for _ in range(n_queries):
        name1, _, name2 = [x.lower() for x in input().split()]
        graph[name1].append(name2)
        graph[name2].append(name1)
    dfs(FIRST, None)
    print(dist[FIRST])
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()