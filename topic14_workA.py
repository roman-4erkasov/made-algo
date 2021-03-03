"""
A. Сравнения подстрок
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Дана строка s. Ответьте на m запросов вида: равны ли подстроки s[a..b] и s[c..d].

Входные данные
В первой строке ввода записана строка s (1 ≤ |s| ≤ 105).

Во второй строке записано целое число m — количество запросов (0 ≤ m ≤ 105).

В следующих m строках четверки чисел a, b, c, d (1 ≤ a ≤ b ≤ |s|, 1 ≤ c ≤ d ≤ |s|).

Выходные данные
Выведите m строк. Выведите Yes, если подстроки совпадают, и No иначе.

Пример
входные данныеСкопировать
trololo
3
1 7 1 7
3 5 5 7
1 1 1 5
выходные данныеСкопировать
Yes
Yes
No

"""
import random
import sys
 
PRIME1 = 10 ** 9 + 7
PRIME2 = 10 ** 9 + 9
POW_0 = 1  # число в нулевой степени
EMPTY = 0  # не заполненный слот для степени
 
 
def safe_mod(value, modulo):
    return ((value % modulo) + modulo) % modulo
 
 
def compute_prefix_hashes(string, x, prime):
    result = [None for _ in range(len(string) + 1)]
    result[0] = 0
    for i, c in enumerate(string, 1):
        result[i] = (result[i - 1] * x + ord(c)) % prime
    return result
 
 
def compute_hash(prefix_hashes, powers, prime, start, finish):
    length = finish - start + 1
    diff = prefix_hashes[finish] - prefix_hashes[start - 1] * powers[length]
    return safe_mod(diff, prime)
 
 
def compute_powers(length, prime):
    # noinspection PyTypeChecker
    result = [POW_0] + [EMPTY] * length
 
    for i in range(1, len(string) + 1):
        result[i] = safe_mod(result[i - 1] * x, prime)
 
    return result
 
 
if __name__ == '__main__':
    x = random.randint(1, max(PRIME1, PRIME2))
    string = sys.stdin.readline()
    n_queries = int(sys.stdin.readline())
    string_len = len(string)
 
    prefix_hashes_1 = compute_prefix_hashes(string, x, PRIME1)
    prefix_hashes_2 = compute_prefix_hashes(string, x, PRIME2)
 
    powers1 = compute_powers(string_len, PRIME1)
    powers2 = compute_powers(string_len, PRIME2)
 
    for _ in range(n_queries):
        start_left, finish_left, start_right, finish_right = map(
            int, sys.stdin.readline().split())
        len_left = finish_left - start_left + 1
        len_right = finish_right - start_right + 1
 
        if len_left == len_right:
            h1_left = compute_hash(
                prefix_hashes=prefix_hashes_1,
                prime=PRIME1,
                start=start_left,
                finish=finish_left,
                powers=powers1
            )
            h2_left = compute_hash(
                prefix_hashes=prefix_hashes_2,
                prime=PRIME2,
                start=start_left,
                finish=finish_left,
                powers=powers2
            )
 
            h1_right = compute_hash(
                prefix_hashes=prefix_hashes_1,
                prime=PRIME1,
                start=start_right,
                finish=finish_right,
                powers=powers1
            )
            h2_right = compute_hash(
                prefix_hashes=prefix_hashes_2,
                prime=PRIME2,
                start=start_right,
                finish=finish_right,
                powers=powers2
            )
 
            print("Yes" if (h1_left == h1_right)
                  and (h2_left == h2_right) else "No")
        else:
            print("No")