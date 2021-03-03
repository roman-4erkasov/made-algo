/**
B. Сортировка подсчетом
ограничение по времени на тест1 секунда
ограничение по памяти на тест64 мегабайта
вводстандартный ввод
выводстандартный вывод
Дан список из N элементов, которые принимают целые значения от 0 до 100. Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.

Входные данные
На одной строке дан массив из N элементов. (1 ≤ N ≤ 2·105) — количество элементов в массиве. Гарантируется, что все элементы массива принимают целые значения от 0 до 100.

Выходные данные
Выведите отсортированный список элeментов

Пример
входные данныеСкопировать
7 3 4 2 5
выходные данныеСкопировать
2 3 4 5 7 
Примечание
Использовать встроенные функции сортировки нельзя.  
**/

#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>
 
#define MAX_VALUE 100
 
void countsort(std::vector<short> &arr, short max_value = 100) {
  unsigned long long counter[max_value], arr_size = arr.size();
  for (short i = 0; i < max_value; i++) counter[i] = 0;
  for (unsigned long long i = 0; i < arr_size; ++i) counter[arr[i]] += 1;
 
  unsigned long index_trg = 0;
  for (short number = 0; number < max_value; ++number)
    for (unsigned long long dummy = 0; dummy < arr[number]; ++dummy)
      arr[index_trg++] = number;
}
 
int main() {
  std::string buff;
  std::vector<unsigned long long> counter(MAX_VALUE + 1, 0);
  unsigned long long vec_size = 0;
 
  getline(std::cin, buff);
  std::istringstream sstream(buff);
  short number;
  while (sstream >> number) {
    counter[number] += 1;
    vec_size++;
  }
 
  std::vector<short> vec(vec_size, 0);
  unsigned long long index_trg = 0;
  for (short number = 0; number <= MAX_VALUE; ++number)
    for (unsigned long long dummy = 0; dummy < counter[number]; ++dummy)
      vec[index_trg++] = number;
  std::copy(vec.begin(), vec.end(),
            std::ostream_iterator<short>(std::cout, " "));
  std::cout << "\n";
}