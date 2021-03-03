"""
B. Черепаха и монеты
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Черепаха хочет переползти из левого верхнего угла поля размером 𝑛 на 𝑚 клеток (2≤𝑛,𝑚≤1000) в правый нижний. За один шаг она может переместиться на соседнюю клетку вправо или на соседнюю клетку вниз. Кроме того, проходя через каждую клетку, Черепаха получает (или теряет) несколько золотых монет (это число известно для каждой клетки).

Определите, какое максимальное количество монет может собрать Черепаха по пути и как ей нужно идти для этого.

Входные данные
В первой строке вводятся два натуральных числа: 𝑛 и 𝑚 (2≤𝑛,𝑚≤1000), разделённые пробелом. В каждой из следующих 𝑛 строк записаны через пробел по 𝑚 чисел 𝑎𝑖𝑗(|𝑎𝑖𝑗|≤10), которые обозначают количество монет, получаемых Черепашкой при проходе через каждую клетку. Если это число отрицательное, Черепашка теряет монеты.

Выходные данные
В первой строке программа должна вывести наибольшее количество монет, которое может собрать Черепаха. Во второй строке без пробелов выводятся команды, которые нужно выполнить Черепахе: буква 'R' (от слова right) обозначает шаг вправо, а буква 'D' (от слова down) — шаг вниз.

Примеры
входные данныеСкопировать
3 3
0 2 -3
2 -5 7
1 2 0
выходные данныеСкопировать
6
RRDD
входные данныеСкопировать
4 5
4 5 3 2 9
4 6 7 5 9
5 2 5 -3 -10
3 5 2 9 3
выходные данныеСкопировать
41
RDRDDRR

"""

from queue import deque
 
 
def solution(board, N, M):
    curr2prev = dict()
    for row in range(0, N):
        for col in range(0, M):
            if row == 0 and col > 0:
                curr2prev[(row, col)] = (row, col - 1, "R")
                board[row][col] = board[row][col] + board[row][col - 1]
            if col == 0 and row > 0:
                curr2prev[(row, col)] = (row - 1, col, "D")
                board[row][col] = board[row][col] + board[row - 1][col]
            if row > 0 and col > 0:
                if board[row][col - 1] > board[row - 1][col]:
                    curr2prev[(row, col)] = (row, col - 1, "R")
                    board[row][col] = board[row][col] + board[row][col - 1]
                else:
                    curr2prev[(row, col)] = (row - 1, col, "D")
                    board[row][col] = board[row][col] + board[row - 1][col]
 
    row, col = N - 1, M - 1
    path = deque()
    while (row, col) in curr2prev:
        row_new, col_new, step = curr2prev[(row, col)]
        if row_new < row:
            path.appendleft(step)
        else:
            path.appendleft(step)
        row = row_new
        col = col_new
    return board[N - 1][M - 1], path
 
 
def cli_dialog():
    N, M = [int(x) for x in input().split()]
    board = [
        None for _ in range(N)
    ]
    for row_index in range(N):
        row = [int(x) for x in input().split()]
        board[row_index] = row
    profit, path = solution(board, N, M)
    print(profit)
    print("".join([str(x) for x in path]))
 
 
if __name__ == "__main__":
    cli_dialog()