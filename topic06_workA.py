"""
A. Кузнечик собирает монеты
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Кузнечик прыгает по столбикам, расположенным на одной линии на равных расстояниях друг от друга. Столбики имеют порядковые номера от 1 до 𝑛. В начале Кузнечик сидит на столбике с номером 1 и хочет добраться до столбика с номером 𝑛. Он может прыгнуть вперед на расстояние от 1 до 𝑘 столбиков, считая от текущего.

На каждом столбике Кузнечик может получить или потерять несколько золотых монет (для каждого столбика это число известно). Определите, как нужно прыгать Кузнечику, чтобы собрать наибольшее количество золотых монет. Учитывайте, что Кузнечик не может прыгать назад.

Входные данные
В первой строке вводятся два натуральных числа: 𝑛 и 𝑘 (3≤𝑛≤10000, 1≤𝑘≤10000), разделённые пробелом. Во второй строке записаны через пробел 𝑛−2 целых числа – количество монет, которое Кузнечик получает на каждом столбике, от 2-го до 𝑛−1-го. Если это число отрицательное, Кузнечик теряет монеты. Гарантируется, что все числа по модулю не превосходят 10000.

Выходные данные
В первой строке программа должна вывести наибольшее количество монет, которое может собрать Кузнечик. Во второй строке выводится число прыжков Кузнечика, а в третьей строке – номера всех столбиков, которые посетил Кузнечик (через пробел в порядке возрастания).

Если правильных ответов несколько, выведите любой из них.

Примеры
входные данныеСкопировать
5 3
2 -3 5
выходные данныеСкопировать
7
3
1 2 4 5 
входные данныеСкопировать
10 3
-13 -2 -14 -124 -9 -6 -5 -7
выходные данныеСкопировать
-16
4
1 3 6 8 10 
входные данныеСкопировать
12 5
-5 -4 -3 -2 -1 1 2 3 4 5
выходные данныеСкопировать
14
7
1 6 7 8 9 10 11 12 
"""
from queue import Queue, deque
 
 
def solution(n: int, k: int, coins: list):
    """
    Dynamic programming aproach for The Grasshooper problems
    """
 
    path_best = deque([0])
 
    buff = Queue()
    buff.put(0)
 
    profit_curr = 0
    n_jumps = 0
    while not buff.empty():
        curr = buff.get()
        profit_max_ = None
        jump_best = None
        for delta in range(1, k+1):
            jump = delta + curr
            if jump >= n:
                break
            profit = profit_curr + coins[jump]
            if profit_max_ is None or profit_max_ < profit:
                jump_best = jump
                profit_max_ = profit
                if coins[jump] >= 0:
                    break
        if jump_best is not None:
            profit_curr = profit_max_
            buff.put(jump_best)
            path_best.append(jump_best)
            n_jumps += 1
    return n_jumps, profit_curr, [x for x in path_best]
 
 
def cli_dialog():
    """
    test 1:
    5 3
    2 -3 5
    7
    3
    1 2 4 5 
 
    test 2:
    8 2
    1 2 -1 -1 7 -1
    9
    5
    1 2 3 4 6 8
    """
    N, K = [int(x) for x in input().split()]
    coins = [0] + [int(x) for x in input().split()] + [0]
    n_jumps, max_profit, steps = solution(N, K, coins)
    print(max_profit)
    print(n_jumps)
    print(" ".join([str(x + 1) for x in steps]))
 
 
if __name__ == "__main__":
    cli_dialog()