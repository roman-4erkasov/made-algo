/**
Дан небольшой массив целых чисел. Ваша задача — отсортировать его в порядке неубывания.

Входные данные
В первой строке входного файла содержится число N (1 ≤ N ≤ 1000) — количество элементов в массиве. Во второй строке находятся N целых чисел, по модулю не превосходящих 109.

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

#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<iterator>
 
 
void insert_sort(std::vector<int> &vec) {
    int n = vec.size();
    for (int i = 0; i < n; ++i) {
        int x = vec[i], j = i - 1;
        for (; j >= 0 && vec[j] > x; --j)
            vec[j + 1] = vec[j];
        vec[j + 1] = x;
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
    while (sstream >> elm) vec.push_back(elm);
    insert_sort(vec);
    std::copy(
        vec.begin(),
        vec.end(),
        std::ostream_iterator<int>(std::cout, " "));
    std::cout << "\n";
 
    return 0;
}