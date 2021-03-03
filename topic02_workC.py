"""
C. Цифровая сортировка
ограничение по времени на тест3 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Дано 𝑛 строк, выведите их порядок после 𝑘 фаз цифровой сортировки.

В этой задаче требуется реализовать цифровую сортировку.

Входные данные
В первой строке входного файла содержится число 𝑛 — количество строк, 𝑚 — их длина и 𝑘 – число фаз цифровой сортировки (1≤𝑛≤1000, 1≤𝑘≤𝑚≤1000). В следующих 𝑛 строках находятся сами строки.

Выходные данные
Выведите строки в порядке в котором они будут после 𝑘 фаз цифровой сортировки.

Примеры
входные данныеСкопировать
3 3 1
bbb
aba
baa
выходные данныеСкопировать
aba
baa
bbb
входные данныеСкопировать
3 3 2
bbb
aba
baa
выходные данныеСкопировать
baa
aba
bbb
входные данныеСкопировать
3 3 3
bbb
aba
baa
выходные данныеСкопировать
aba
baa
bbb

"""

CHAR_BIAS = 97  # order of character 'a'
N_DIGITS = 26  # number of digits is length of english alphabet
 
 
def char2num(value):
    return ord(value) - CHAR_BIAS
 
 
def num2char(value):
    return chr(value + CHAR_BIAS)
 
 
def countsort(arr, radix, word_length, verbose=False):
    counter = [[] for _ in range(N_DIGITS)]
    for word in arr:
        key = word[word_length - radix - 1]
        if verbose:
            print(f"countsort: k={key} w={word}")
        counter[key].append(word)
 
    index_trg = 0
    for digit in range(N_DIGITS):
        for word in counter[digit]:
            arr[index_trg] = word
            index_trg += 1
    if verbose:
        print(f"countsort: arr={arr}")
        print(f"countsort: counter={counter}")
 
 
if __name__ == "__main__":
    n_words, word_len, n_phases = [int(v) for v in input().split()]
    arr = []
    for _ in range(n_words):
        arr.append([char2num(c) for c in input()])
    for radix in range(n_phases):
        countsort(arr, radix=radix, word_length=word_len)
    for word in arr:
        print("".join(num2char(x) for x in word))