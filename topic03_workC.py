"""
C. Квадратный корень и квадратный квадрат
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Найдите такое число x, что , с точностью не менее 6 знаков после точки.

Входные данные
В единственной строке содержится вещественное число 1.0 ≤ C ≤ 1010.

Выходные данные
Выведите одно число — искомый x.

Примеры
входные данныеСкопировать
2.0000000000
выходные данныеСкопировать
1.0
входные данныеСкопировать
18.0000000000
выходные данныеСкопировать
4.0

"""


EPS = 1e-7
MAX_FINISH = 1e10
 
def function(x, c):
    return x * x + x ** 0.5 - c
 
 
def bin_search(c):
    start = 1.
    finish = MAX_FINISH
    while abs(finish - start) > EPS:
        mid = start + (finish - start) / 2.
        value = function(mid, c)
        if value == c:
            return value
        elif value < 0:
            start = mid
        else:
            finish = mid
    return start + (finish - start) / 2.
 
 
def cli_dialog():
    value = float(input())
    print(f"{bin_search(value):.6f}")
 
 
if __name__ == "__main__":
    cli_dialog()