#####################################
#  задание в одноимённом pdf файле  #
#####################################

def evaluate_roman_digit(digit):
    if digit == 'I':
        return 1
    elif digit == 'V':
        return 5
    elif digit == 'X':
        return 10
    elif digit == 'L':
        return 50
    elif digit == 'C':
        return 100
    elif digit == 'D':
        return 500
    elif digit == 'M':
        return 1000
    else:
        raise Exception(f"digit={digit}")
 
 
def evaluate_roman_number(number):
    n = len(number)
    if n == 0:
        return 0
    elif n == 1:
        return evaluate_roman_digit(number[0])
    elif n > 1:
        result = 0
        index = 0
        while index < n:
            digit_lag = evaluate_roman_digit(number[index])
            if index + 1 < n:
                digit = evaluate_roman_digit(number[index + 1])
                if digit_lag >= digit:
                    result += digit_lag
                    index += 1
                else:
                    result += (digit - digit_lag)
                    index += 2
            else:
                result += digit_lag
                index += 1
        return result
 
 
def merge(vec, head, mid, tail, get_item):
    len_left = mid - head + 1
    len_right = tail - mid
    result = 0
 
    arr_left = vec[head:head + len_left]
    arr_right = vec[mid + 1:mid + 1 + len_right]
 
    idx_left = 0
    idx_right = 0
    idx_target = head
    while idx_left < len_left and idx_right < len_right:
        if get_item(arr_left[idx_left]) > get_item(arr_right[idx_right]):
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
 
 
def merge_sort(vec, get_item):
    n = len(vec)
    result = 0
    step = 1
    while step < n:
        head = 0
        while head < n - 1:
            mid = head + step - 1
            tail = min(head + 2 * step - 1, n - 1)
            if mid < tail:
                result += merge(vec, head, mid, tail, get_item)
            head += 2 * step
        step *= 2
    return result
 
 
if __name__ == '__main__':
    n = int(input())
    names = []
    for _ in range(n):
        name, rom_num = input().split()
        value = evaluate_roman_number(rom_num)
        names.append((name, rom_num, value))
    merge_sort(names, lambda x: x[2])
    merge_sort(names, lambda x: x[0])
    print(
        "\n".join(
            [name + " " + rom_num for name, rom_num, _ in names]
        )
    )
