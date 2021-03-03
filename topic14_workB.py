"""
B. Z-функция
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Постройте Z-функцию для заданной строки s.

Входные данные
Первая строка входного файла содержит s (1 ≤ |s| ≤ 106). Строка состоит из букв латинского алфавита.

Выходные данные
Выведите значения Z-функции строки s для индексов 2, 3, ..., |s|.

Примеры
входные данныеСкопировать
aaaAAA
выходные данныеСкопировать
 2 1 0 0 0
входные данныеСкопировать
abacaba
выходные данныеСкопировать
 0 1 0 3 0 1

"""

def z_fun(string):
    start = 0
    finish = 0
    n = len(string)
    result = [0 for _ in range(n)]
    for idx in range(1, n):
        result[idx] = max(0, min(finish - idx, result[idx - start]))
        while idx + result[idx] < n and string[result[idx]] == string[idx + result[idx]]:
            result[idx] += 1
        if idx + result[idx] > finish:
            start = idx
            finish = idx + result[idx]
    return result
 
 
def main():
    string = input()
    res = z_fun(string)
    print(" ".join([str(x) for x in res[1:]]))
 
 
if __name__ == '__main__':
    main()