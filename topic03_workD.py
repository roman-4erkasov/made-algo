"""
D. Веревочки
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
С утра шел дождь, и ничего не предвещало беды. Но к обеду выглянуло солнце, и в лагерь заглянула СЭС. Пройдя по всем домикам и корпусам, СЭС вынесла следующий вердикт: бельевые веревки в жилых домиках не удовлетворяют нормам СЭС. Как выяснилось, в каждом домике должно быть ровно по одной бельевой веревке, и все веревки должны иметь одинаковую длину. В лагере имеется N бельевых веревок и K домиков. Чтобы лагерь не закрыли, требуется так нарезать данные веревки, чтобы среди получившихся веревочек было K одинаковой длины. Размер штрафа обратно пропорционален длине бельевых веревок, которые будут развешены в домиках. Поэтому начальство лагеря стремиться максимизировать длину этих веревочек.

Входные данные
В первой строке заданы два числа — N и K (1 ≤ N, K ≤ 10001). Далее в каждой из последующих N строк записано по одному числу — длине очередной бельевой веревки. Длина веревки задана в сантиметрах. Все длины лежат в интервале от 1 сантиметра до 100 километров включительно.

Выходные данные
В выходной файл следует вывести одно целое число — максимальную длину веревочек, удовлетворяющую условию, в сантиметрах. В случае, если лагерь закроют, выведите 0.

Пример
входные данныеСкопировать
4 11
802
743
457
539
выходные данныеСкопировать
200

"""

import random
 
 
def function(ropes, n_required, min_length):
    n = 0
    for rope in ropes:
        if rope == min_length:
            n += 1
        elif rope > min_length:
            n += rope // min_length
    return n >= n_required
 
 
def lower_bound(array, query):
    beg = 0  # because min value is 1, not 0
    min_rope = None
    for rope in array:
        if min_rope is None or rope > min_rope:
            min_rope = rope
    end = min_rope + 1
    # substraction of just added 1 to express invariant explicitly
    while beg < end - 1:
        mid = (beg + end) // 2
        value = function(
            ropes=array,
            n_required=query,
            min_length=mid
        )
        if not value:
            end = mid
        else:
            beg = mid
    return end
 
 
def naive_solution(ropes, query):
    beg = 1
    end = None
    for rope in ropes:
        if end is None or rope > end:
            end = rope
 
    while beg < end:
        mid = beg + (end - beg) // 2
        value = function(
            ropes=ropes,
            n_required=query,
            min_length=mid
        )
        if not value:
            end = mid
        else:
            beg = mid + 1
 
    if not function(
            ropes=ropes,
            n_required=query,
            min_length=beg
    ):
        result = beg - 1
    else:
        result = beg
    return result
 
 
def test(n_trials=100):
    min_value = 1
    max_value = 1000
    max_length = 10
    for n_success in range(n_trials):
        n = random.randint(a=1, b=max_length)
        qry = random.randint(
            a=min_value,
            b=max_value
        )
        vec = [
            random.randint(a=min_value, b=max_value)
            for _ in range(n)
        ]
        expected = naive_solution(vec, qry)
        actual = lower_bound(vec, qry) - 1
        msg = f"vec={vec} qry={qry} exp={expected} act={actual} success={n_success}"
        assert expected == actual, msg
 
 
def cli_dialog():
    n, k = [int(x) for x in input().split()]
    ropes = []
    for _ in range(n):
        ropes.append(int(input()))
    print(max(0, lower_bound(ropes, k) - 1))
 
 
if __name__ == "__main__":
    cli_dialog()
    # test()