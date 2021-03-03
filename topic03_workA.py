"""
A. Приближенный двоичный поиск
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Даны два массива. Первый массив отсортирован по неубыванию, второй массив содержит запросы — целые числа.

Для каждого запроса выведите число из первого массива наиболее близкое (то есть с минимальным модулем разности) к числу в этом запросе . Если таких несколько, выведите меньшее из них.

Входные данные
В первой строке входных данных содержатся числа n и k (0 < n, k ≤ 105). Во второй строке задаются n чисел первого массива, отсортированного по неубыванию, а в третьей строке — k чисел второго массива. Каждое число в обоих массивах по модулю не превосходит 2·109 .

Выходные данные
Для каждого из k чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному. Если таких несколько, выведите меньшее из них.

Пример
входные данныеСкопировать
5 5
1 3 5 7 9
2 4 8 1 6
выходные данныеСкопировать
1
3
7
1
5

"""

import random
 
 
def lower_bound(array, query):
    beg = -1
    end = len(array)
    while beg < end - 1:
        mid = (beg + end) // 2
        if query <= array[mid]:
            end = mid
        else:
            beg = mid
    return end
 
 
def solve(array, query, verbose=0):
    if len(array) == 1:
        return array[0]
    lb = lower_bound(array, query)
    if lb == len(array) or array[lb] != query:
        lb = max(0, lb - 1)
    ub = min(lb + 1, len(array) - 1)
    if verbose:
        print(f"x={query} lb={lb} ub={ub}")
    if 0 <= lb and abs(array[lb] - query) <= abs(array[ub] - query):
        idx_result = lb
    else:
        idx_result = ub
    return array[idx_result]
 
 
def naively_solve(array, query):
    def lower_bound(array, query):
        beg = 0
        end = len(array)
        while beg < end:
            mid = beg + (end - beg) // 2
            if array[mid] < query:
                beg = mid + 1
            else:
                end = mid
        return beg
 
    def upper_bound(array, query):
        beg = 0
        end = len(array)
        while beg < end:
            mid = beg + (end - beg) // 2
            if query < array[mid]:
                end = mid
            else:
                beg = mid + 1
        return beg
 
    def clip_index(index, max_value):
        if index < 0:
            index = 0
        if index > max_value:
            index = max_value
        return index
 
    if len(array) == 1:
        return array[0]
    n = len(array)
    lb = lower_bound(array, query)
    if 0 < lb < n and array[lb] > query:
        lb -= 1
    lb = clip_index(lb, n - 1)
    ub = clip_index(upper_bound(array, query), n - 1)
    if abs(array[lb] - query) <= abs(array[ub] - query):
        idx_result = lb
    else:
        idx_result = ub
    return array[idx_result]
 
 
def test(n_trials=100):
    min_value = -2_000_000_000
    max_value = 2_000_000_000
    max_length = 100000
    for _ in range(n_trials):
        n = random.randint(a=1, b=max_length)
        qry = random.randint(
            a=min_value,
            b=max_value
        )
        vec = sorted([
            random.randint(a=min_value, b=max_value)
            for _ in range(n)
        ])
        try:
            expected = naively_solve(vec, qry)
        except Exception:
            print(f"vec={vec} qry={qry}")
            raise
        try:
            actual = solve(vec, qry)
        except Exception:
            print(f"vec={vec} qry={qry}")
            raise
        msg = f"vec={vec} qry={qry} exp={expected} act={actual}"
        assert expected == actual, msg
 
 
def test_case():
    vec = [-16, -6, -6, -4]
    qry = -18
    actual = solve(vec, qry)
    print(actual)
 
 
def cli_dialog():
    _ = input()
    arr = [int(x) for x in input().split()]
    queries = [int(x) for x in input().split()]
    result = []
    for qry in queries:
        result.append(str(solve(arr, qry)))
    print("\n".join(result))
 
 
if __name__ == "__main__":
    cli_dialog()
    # test()
    # test_case()