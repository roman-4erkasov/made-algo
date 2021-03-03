/**
𝑘 -я имперская порядковая статистика
ограничение по времени на тест1.2 секунд
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Батальон клонов вышел на построение. Все имперцы стали в один ряд и пересчитались: первый, второй, третий, …, 𝑛-й. Каждый из них держит в руках бумажку с результатом своего тестирования IQ. Как известно, результатом тестирования IQ является число от 1 до 109.

Периодически к батальону подходит граф Дуко, размахивает мечом и делает запрос: «Если всех клонов с 𝑖-го по 𝑗-го упорядочить по результату теста, то какое значение будет у клона, стоящем на 𝑘-м месте?» — и быстро требует ответ, грозя всю партию пустить в расход. Большая просьба — решите эту задачу и помогите клонам выжить.

Входные данные
В первой строке входного файла содержится целое число 𝑛 — количество клонов (1≤𝑛≤1000).

Во второй строке содержатся эти 𝑛 целых чисел, разделённые пробелами. Числа находятся в промежутке от 1 до 109.

В третьей строке содержится число 𝑚 — количество запросов (1≤𝑚≤105).

Последние 𝑚 строк содержат запросы в формате «𝑖 𝑗 𝑘». Гарантируется, что запросы корректны, то есть 1≤𝑖≤𝑗≤𝑛 и на отрезке от 𝑖-го до 𝑗-го элемента включительно есть хотя бы 𝑘 элементов.

Выходные данные
На каждый запрос выведите единственное число — ответ на запрос.

Пример
входные данныеСкопировать
5
1 3 2 4 5
3
1 3 2
1 5 1
1 5 2
выходные данныеСкопировать
2
1
2

**/

#include <algorithm>
#include <deque>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
 
long partition(std::vector<long> &vec, long head, long tail) {
  long idx_border = head - 1;
  long pivot = vec[tail];
  long idx_check = head;
  for (; idx_check <= tail - 1; idx_check++) {
    if (vec[idx_check] <= pivot) {
      std::swap(vec[idx_check], vec[++idx_border]);
    }
  }
  std::swap(vec[idx_check], vec[++idx_border]);
  return idx_border;
}
 
long kth_elem(std::vector<long> vec, long k) {
  long result = -1;
  std::pair<long, long> pair;
  std::deque<std::pair<long, long>> buff = std::deque<std::pair<long, long>>();
  buff.push_back(std::make_pair(0, vec.size() - 1));
  while (not buff.empty()) {
    pair = buff.front();
    buff.pop_front();
    long pivot = partition(vec, pair.first, pair.second);
    if (pivot == k) {
      result = vec[pivot];
      break;
    } else if (pivot > k)
      buff.push_back(std::make_pair(pair.first, pivot - 1));
    else
      buff.push_back(std::make_pair(pivot + 1, pair.second));
  }
  return result;
}
 
int main() {
  long n, n_qry, start, k, finish;
  std::string buff;
  std::vector<long> vec;
 
  std::cin >> n;
  std::cin.ignore();
 
  getline(std::cin, buff);
  std::istringstream sstream(buff);
  long elm;
  while (sstream >> elm) vec.push_back(elm);
  std::cin >> n_qry;
 
  for (size_t i = 0; i < n_qry; i++) {
    std::cin >> start >> finish >> k;
    start--;
    finish--;
    k--;
    std::vector<long> sub(vec.begin() + start, vec.begin() + finish + 1);
    long res = kth_elem(sub, k);
    std::cout << res << "\n";
  }
}