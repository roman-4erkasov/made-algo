"""
D. Гриша после дискотеки
ограничение по времени на тест2 секунды
ограничение по памяти на тест512 мегабайт
вводстандартный ввод
выводстандартный вывод
На следующий день после дискотеки Гриша решил устроить детям «взрыв мозга». Он взял много карточек и написал на каждой из них одну латинскую букву в нижнем регистре. А после этого придумал свою строку и задал детям задание: составить как можно больше подстрок своей строки, используя карточки. Гришина строка состоит только из букв латинского алфавита в нижнем регистре. Вам нужно определить сколько её подстрок можно составить, используя только данные карточки.

Запишем буквы, написанные на карточках, подряд друг за другом. Тогда если Гришина строка — это «aaab», а карточки — это «aba», то можно составить три подстроки «a», подстроку «b», две подстроки «aa» и подстроки «ab» и «aab». А подстроки «aaa» и «aaab» нельзя, так как есть всего две карточки с буквой «a».

Входные данные
Первая строка входных данных содержит два целых числа 𝑛 и 𝑚 (1≤𝑛,𝑚≤105) — длину строки Гриши и длину строки карточек.

Вторая строка входных данных содержит Гришину строку 𝑠 длины 𝑛, состоящую только из букв латинского алфавита в нижнем регистре.

Третья строка входных данных содержит строку карточек 𝑡 длины 𝑚, состоящую только из букв латинского алфавита в нижнем регистре.

Выходные данные
Выведите одно целое число — количество подстрок в 𝑠, которые можно составить из символов строки 𝑡.

Примеры
входные данныеСкопировать
4 3
aaab
aba
выходные данныеСкопировать
8
входные данныеСкопировать
7 3
abacaba
abc
выходные данныеСкопировать
15

"""

from collections import deque
 
CHAR_BIAS = 97  # order of character 'a'
N_DIGITS = 26  # number of digits is length of english alphabet
 
 
def char2num(value):
    return ord(value) - CHAR_BIAS
 
 
def num2char(value):
    return chr(value + CHAR_BIAS)
 
 
def count_subwords(main_string, card_string, n_main):
    if main_string == card_string:
        return n_main * (n_main + 1) // 2
 
    result = 0
 
    main_arr = [char2num(c) for c in main_string]
    main_counter = [0 for _ in range(N_DIGITS + 1)]
    for num in main_arr:
        main_counter[num] += 1
 
    card_arr = [char2num(c) for c in card_string]
    card_counter = [0 for _ in range(N_DIGITS + 1)]
    for num in card_arr:
        card_counter[num] += 1
 
    # if counters are equal then computation is simple
    counters_eq = True
    for i in range(N_DIGITS):
        if card_counter[i] != main_counter[i]:
            counters_eq = False
            break
    if counters_eq:
        return n_main * (n_main + 1) // 2
 
    index_start = 0
    index_finish = 0
    buff = deque([main_arr[0]])
    counts = card_counter.copy()
    while index_start < n_main:
        num = buff[-1]
        if counts[num] > 0:
            counts[num] = counts[num] - 1
            result += index_finish - index_start + 1
            if index_finish < n_main - 1:
                index_finish += 1
                buff.append(main_arr[index_finish])
            else:
                break
        else:
            num = buff.popleft()
            if counts[num] < card_counter[num]:
                counts[num] = counts[num] + 1
            if index_start < n_main - 1:
                index_start += 1
                if index_finish < index_start:
                    index_finish = index_start
                    buff.append(main_arr[index_finish])
            else:
                break
    return result
 
 
if __name__ == "__main__":
    main_len, n_cards = [int(x) for x in input().split()]
    main_str = input()
    card_str = input()
    print(count_subwords(main_str, card_str, main_len))