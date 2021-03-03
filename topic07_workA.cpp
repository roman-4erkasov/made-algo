/**
A. Сумма простая
ограничение по времени на тест1 секунда
ограничение по памяти на тест512 мегабайт
вводстандартный ввод
выводстандартный вывод
Вам нужно научиться отвечать на запрос «сумма чисел на отрезке».

Массив не меняется. Запросов много. Отвечать на каждый запрос следует за .

Входные данные
Размер массива — n и числа x, y, a0, порождающие массив a: 

Далее следует количество запросов m и числа z, t, b0, порождающие массив b: .

Массив c строится следующим образом: .

Запросы: i-й из них — найти сумму на отрезке от min(c2i, c2i + 1) до max(c2i, c2i + 1) в массиве a.

Ограничения: 1 ≤ n ≤ 107, 0 ≤ m ≤ 107. Все числа целые от 0 до 216. t может быть равно  - 1.

Выходные данные
Выведите сумму всех сумм.

Пример
входные данныеСкопировать
3 1 2 3
3 1 -1 4
выходные данныеСкопировать
23
Примечание
a = {3, 5, 7}, b = {4, 3, 2, 1, 0, 230 - 1}, c = {1, 0, 2, 1, 0, 0},

запросы = {[0, 1], [1, 2], [0, 0]}, суммы = {8, 12, 3}.
**/
#include <math.h>
 
#include <iostream>
#include <vector>
 
const unsigned long long MOD_A = (unsigned long long)powl(2, 16);
const unsigned long long MOD_B = (unsigned long long)powl(2, 30);
 
unsigned long long get_next_linear(unsigned long long old_value,
                                   unsigned long long scale,
                                   unsigned long long bias) {
  unsigned long long result = scale * old_value + bias;
  return result;
}
 
unsigned long long get_mod(unsigned long long value,
                           unsigned long long modulo) {
  unsigned long long result = value % modulo;
  if (result < 0) {
    result += modulo;
  }
  return result;
}
 
void cli_dialog() {
  unsigned long long result = 0;
  unsigned long long len, x, y, a0, n_qry, z, b0;
  long long t;
 
  std::cin >> len >> x >> y >> a0;
  std::cin >> n_qry >> z >> t >> b0;
 
  unsigned long long n_max = std::max(2 * n_qry, len);
  std::vector<unsigned long long> arr_a(len), arr_b(2 * n_qry),
      arr_c(2 * n_qry);
  if (n_qry > 0) {
    arr_a[0] = a0;
    arr_b[0] = b0;
    arr_c[0] = get_mod(b0, len);
    for (size_t i = 1; i < n_max; i++) {
      if (i < len) {
        arr_a[i] = get_mod(get_next_linear(arr_a[i - 1], x, y), MOD_A);
      }
      if (i < 2 * n_qry) {
        arr_b[i] = get_mod(get_next_linear(arr_b[i - 1], z, t), MOD_B);
        arr_c[i] = get_mod(arr_b[i], len);
      }
    }
 
    std::vector<unsigned long long> sum_a(len);
    sum_a[0] = arr_a[0];
    for (size_t i = 1; i < arr_a.size(); i++) {
      sum_a[i] = sum_a[i - 1] + arr_a[i];
    }
 
    for (size_t i = 0; i < n_qry; i++) {
      unsigned long long left = std::min(arr_c[2 * i], arr_c[2 * i + 1]),
                         right = std::max(arr_c[2 * i], arr_c[2 * i + 1]);
      if (left == 0) {
        result += sum_a[right];
      } else {
        result += (sum_a[right] - sum_a[left - 1]);
      }
    }
  }
  std::cout << result << "\n";
}
 
int main() {
  cli_dialog();
  return 0;
}