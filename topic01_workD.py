"""
D. Количество инверсий
ограничение по времени на тест 5 секунд
ограничение по памяти на тест 256 мегабайт
вводстандартный ввод
выводстандартный вывод
Напишите программу, которая для заданного массива 𝐴=⟨𝑎1,𝑎2,…,𝑎𝑛⟩ находит количество пар (𝑖,𝑗) таких, что 𝑖<𝑗 и 𝑎𝑖>𝑎𝑗.

Входные данные
Первая строка входного файла содержит натуральное число 𝑛 (1≤𝑛≤500000) — количество элементов массива. Вторая строка содержит 𝑛 попарно различных элементов массива 𝐴 (0≤𝑎𝑖≤106).

Выходные данные
В выходной файл выведите одно число — ответ на задачу.

Примеры
входные данныеСкопировать
4
1 2 4 5
выходные данныеСкопировать
0
входные данныеСкопировать
4
5 4 2 1
выходные данныеСкопировать
6

"""


def merge(vec, head, mid, tail):
    len_left = mid - head + 1
    len_right = tail - mid
    result = 0
 
    arr_left = vec[head:head + len_left]
    arr_right = vec[mid + 1:mid + 1 + len_right]
 
    idx_left = 0
    idx_right = 0
    idx_target = head
    while idx_left < len_left and idx_right < len_right:
        if arr_left[idx_left] > arr_right[idx_right]:
            vec[idx_target] = arr_right[idx_right]
            idx_right += 1
            result += len_left - idx_left
        else:
            vec[idx_target] = arr_left[idx_left]
            idx_left += 1
        idx_target += 1
    while idx_left < len_left:
        vec[idx_target] = arr_left[idx_left]
        idx_left += 1
        idx_target += 1
    while idx_right < len_right:
        vec[idx_target] = arr_right[idx_right]
        idx_right += 1
        idx_target += 1
    return result
 
 
def merge_sort(vec):
    n = len(vec)
    result = 0
    step = 1
    while step < n:
        head = 0
        while head < n - 1:
            mid = head + step - 1
            tail = min(head + 2 * step - 1, n - 1)
            if mid < tail:
                result += merge(vec, head, mid, tail)
            head += 2 * step
        step *= 2
    return result
 
 
if __name__ == '__main__':
    n = int(input())
    vec = [int(x) for x in input().split()]
    print(merge_sort(vec))