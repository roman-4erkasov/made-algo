"""
C. Быстрый поиск подстроки в строке
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Даны строки p и t. Требуется найти все вхождения строки p в строку t в качестве подстроки.

Входные данные
Первая строка входного файла содержит p, вторая — t (1 ≤ |p|, |t| ≤ 106). Строки состоят из букв латинского алфавита.

Выходные данные
В первой строке выведите количество вхождений строки p в строку t. Во второй строке выведите в возрастающем порядке номера символов строки t, с которых начинаются вхождения p. Символы нумеруются с единицы.

Пример
входные данныеСкопировать
aba
abaCaba
выходные данныеСкопировать
2
1 5

"""

def pfun(string):
    length = len(string)
    prefix = [0 for _ in range(length)]
    for i in range(1, length):
        k = prefix[i - 1]
        while k > 0 and string[i] != string[k]:
            k = prefix[k - 1]
        if string[i] == string[k]:
            k += 1
        prefix[i] = k
    return prefix
 
 
def kmp(sub, string):
    SEP = "#"
    len_sub = len(sub)
    s = sub + SEP + string
    p = pfun(s)
    result = [i - 2 * len_sub for i, x in enumerate(p) if x == len_sub]
    return result
 
 
def main():
    sub = input()
    string = input()
    res = kmp(sub, string)
    print(len(res))
    print(" ".join([str(x + 1) for x in res]))
 
 
if __name__ == '__main__':
    main()