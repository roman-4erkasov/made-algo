"""
E. Очень Легкая Задача
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Сегодня утром жюри решило добавить в вариант олимпиады еще одну, Очень Легкую Задачу. Ответственный секретарь Оргкомитета напечатал ее условие в одном экземпляре, и теперь ему нужно до начала олимпиады успеть сделать еще n копий. В его распоряжении имеются два ксерокса, один из которых копирует лист за x секунд, а другой — за y. (Разрешается использовать как один ксерокс, так и оба одновременно. Можно копировать не только с оригинала, но и с копии.) Помогите ему выяснить, какое минимальное время для этого потребуется.

Входные данные
На вход программы поступают три натуральных числа n, x и y, разделенные пробелом (1 ≤ n ≤ 2·108, 1 ≤ x, y ≤ 10).

Выходные данные
Выведите одно число — минимальное время в секундах, необходимое для получения n копий.

Примеры
входные данныеСкопировать
4 1 1
выходные данныеСкопировать
3
входные данныеСкопировать
5 1 2
выходные данныеСкопировать
4

"""
import sys
from math import gcd
 
 
def is_enough(duration_min, duration_max, n_required,
              time_available, verbose=False):
    mult_min = duration_min / (duration_min + duration_max)
    mult_max = duration_max / (duration_min + duration_max)
 
    n_max = int((n_required - 1) * mult_min)
    n_min = int((n_required - 1) * mult_max)
 
    min_time: int = None
    if n_min + n_max == n_required - 1:
        min_time = max(
            duration_min * n_min,
            duration_max * n_max
        )
    elif n_min + 1 + n_max == n_required - 1:
        val = max(
            duration_min * (n_min + 1),
            duration_max * n_max
        )
 
        if (min_time is None) or (val < min_time):
            min_time = val
        val = max(
            duration_min * n_min,
            duration_max * (n_max + 1)
        )
        if (min_time is None) or (val < min_time):
            min_time = val
    elif n_min + 2 + n_max == n_required - 1:
        val = max(
            duration_min * (n_min + 1),
            duration_max * (n_max + 1)
        )
        if (min_time is None) or (val < min_time):
            min_time = val
    if min_time is not None:
        min_time += duration_min
    return min_time <= time_available
 
 
def solution(work_durations, n_required, verbose=False):
    duration_min = min(work_durations)
    duration_max = max(work_durations)
 
    if n_required == 1:
        return duration_min
 
    beg = duration_min * n_required // 2 - 1
    end = duration_max * n_required + 1
 
    # substraction of just added 1 is to express invariant explicitly
    while beg < end - 1:
        mid = (beg + end) // 2
        if verbose:
            print(f"b={beg} m={mid} e={end}")
        value = is_enough(
            duration_min=duration_min, duration_max=duration_max,
            n_required=n_required,
            time_available=mid,
            verbose=verbose
        )
        if verbose:
            print(f"lower: is_enough={value} mid={mid}")
        if value:
            end = mid
        else:
            beg = mid
    return end
 
 
def naive_solution(work_durations, n_required, verbose=False):
    duration_min = min(work_durations)
    duration_max = max(work_durations)
 
    if n_required == 1:
        return duration_min
 
    beg = duration_min * n_required // 2
    end = duration_max * n_required
 
    while beg < end:
        mid = beg + (end - beg) // 2
        if verbose:
            print(f"b={beg} m={mid} e={end}")
        value = is_enough(
            duration_min=duration_min, duration_max=duration_max,
            n_required=n_required,
            time_available=mid,
            verbose=verbose
        )
        if verbose:
            print(f"lower: is_enough={value} mid={mid}")
        if not value:
            beg = mid + 1
        else:
            end = mid
    return beg
 
 
def cli_dialog():
    n_copies, first_printer, second_printer = \
        [int(x) for x in sys.stdin.readline().split()]
    sys.stdout.write(
        str(
            solution(
                work_durations=[first_printer, second_printer],
                n_required=n_copies
            )
        ) + "\n"
    )
 
 
if __name__ == "__main__":
    cli_dialog()