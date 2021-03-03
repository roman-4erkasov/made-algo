/**

Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания.

Входные данные
В первой строке входного файла содержится число N (1 ≤ N ≤ 100 000) — количество элементов в массиве. Во второй строке находятся N целых чисел, по модулю не превосходящих 109.

Выходные данные
В выходной файл надо вывести этот же массив в порядке неубывания, между любыми двумя числами должен стоять ровно один пробел.

Пример
входные данныеСкопировать
10
1 8 2 1 4 7 3 2 3 6
выходные данныеСкопировать
1 1 2 2 3 3 4 6 7 8 
Примечание
Запрещается использовать стандартные сортировки.

**/

#include <vector>
#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <algorithm>
 
void merge(std::vector<int> &vec, int head, int mid, int tail) {
    int len_left = mid - head + 1, len_right = tail - mid;
 
    int arr_left[len_left], arr_right[len_right];
    for (int i = 0; i < len_left; ++i)
        arr_left[i] = vec[head + i];
    for (int i = 0; i < len_right; ++i)
        arr_right[i] = vec[mid + i + 1];
 
    int idx_left = 0, idx_right = 0, idx_target = head;
    while (idx_left < len_left && idx_right < len_right) {
        if (arr_left[idx_left] > arr_right[idx_right])
            vec[idx_target] = arr_right[idx_right++];
        else
            vec[idx_target] = arr_left[idx_left++];
        idx_target++;
    }
    while (idx_left < len_left)
        vec[idx_target++] = arr_left[idx_left++];
    while (idx_right < len_right)
        vec[idx_target++] = arr_right[idx_right++];
}
 
void merge_sort_iterative(std::vector<int> &vec) {
    int n = vec.size();
    for (int step = 1; step < n; step *= 2) {
        for (int head = 0; head < n - 1; head += 2 * step) {
            int mid = head + step - 1;
            int tail = std::min(head + 2 * step - 1, n - 1);
            if (mid < tail)
                merge(vec, head, mid, tail);
        }
    }
}
 
int main() {
    std::ios::sync_with_stdio(false);
 
    unsigned int n;
    std::string buff;
    std::vector<int> vec;
 
    std::cin >> n;
    std::cin.ignore();
 
    getline(std::cin, buff);
    std::istringstream sstream(buff);
    int elm;
    while (sstream >> elm)
        vec.push_back(elm);
    merge_sort_iterative(vec);
    std::copy(
        vec.begin(),
        vec.end(),
        std::ostream_iterator<int>(std::cout, " "));
    std::cout << "\n";
 
    return 0;
}
