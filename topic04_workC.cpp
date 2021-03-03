/**
C. Реализуйте очередь
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Для каждой операции изъятия элемента выведите ее результат.

На вход программе подаются строки, содержащие команды. Каждая строка содержит одну команду. Команда — это либо "+ N", либо "-". Команда "+ N" означает добавление в очередь числа 𝑁, по модулю не превышающего 109. Команда "-" означает изъятие элемента из очереди.

Входные данные
В первой строке содержится количество команд — 𝑚 (1⩽𝑚⩽105). В последующих строках содержатся команды, по одной в каждой строке.

Выходные данные
Выведите числа, которые удаляются из очереди, по одному в каждой строке. Гарантируется, что изъятий из пустой очереди не производится.

Пример
входные данныеСкопировать
4
+ 1
+ 10
-
-
выходные данныеСкопировать
1
10

**/

#include <iostream>
#include <memory>
#include <sstream>
#include <vector>
 
// for stress testing
#include <stdlib.h>
#include <queue>
 
typedef long long value_t;
typedef unsigned long long index_t;
 
template <typename data_t>
class Queue {
 private:
  unsigned long long length, head, end, growth_factor, capacity,
      size = 0, min_capacity = 2;
  std::unique_ptr<data_t[]> ptr_data;
  bool not_used = true;
 
 public:
  Queue(size_t init_capacity = 2, size_t growth_factor_ = 2);
  std::string to_string();
  void push_back(data_t value);
  void increase_capacity();
  void decrease_capacity();
  data_t pop_front();
  data_t front() { return *(ptr_data.get() + head); }
  unsigned long long get_size() { return size; }
};
 
template <typename data_t>
Queue<data_t>::Queue(size_t init_capacity, size_t growth_factor_)
    : growth_factor(growth_factor_), capacity(init_capacity), head(0), end(0) {
  data_t *p = new data_t[init_capacity];
  ptr_data = std::unique_ptr<data_t[]>(p);
}
 
template <typename data_t>
void Queue<data_t>::increase_capacity() {
  if ((end == head and !not_used) or (head == 0 and end == capacity)) {
    unsigned long long capacity_new = capacity * growth_factor;
    data_t *p = new data_t[capacity_new];
    std::unique_ptr<data_t[]> ptr_data_new = std::unique_ptr<data_t[]>(p);
 
    if (end <= head and !not_used) {
      int insert_idx = 0;
      for (unsigned long long i = head; i < capacity; ++i, ++insert_idx)
        *(ptr_data_new.get() + insert_idx) = *(ptr_data.get() + i);
      for (unsigned long long i = 0; i < end; ++i, ++insert_idx)
        *(ptr_data_new.get() + insert_idx) = *(ptr_data.get() + i);
    } else if (head < end) {
      for (unsigned long long i = head, insert_idx = 0; i < end;
           ++i, ++insert_idx)
        *(ptr_data_new.get() + insert_idx) = *(ptr_data.get() + i);
    }
    head = 0;
    end = size;
    ptr_data = std::move(ptr_data_new);
    capacity = capacity_new;
  }
}
 
template <typename data_t>
void Queue<data_t>::push_back(data_t value) {
  increase_capacity();
  *(ptr_data.get() + end) = value;
  size++;
  end = (end + 1) % capacity;
  not_used = false;
}
 
template <typename data_t>
void Queue<data_t>::decrease_capacity() {
  if (growth_factor * size < capacity and
      capacity / growth_factor >= min_capacity) {
    unsigned long long capacity_new = capacity / growth_factor;
    data_t *p = new data_t[capacity_new];
    std::unique_ptr<data_t[]> ptr_data_new = std::unique_ptr<data_t[]>(p);
 
    if (end <= head and !not_used) {
      int insert_idx = 0;
      for (unsigned long long i = head; i < capacity; ++i, ++insert_idx)
        *(ptr_data_new.get() + insert_idx) = *(ptr_data.get() + i);
 
      for (unsigned long long i = 0; i < end; ++i, ++insert_idx)
        *(ptr_data_new.get() + insert_idx) = *(ptr_data.get() + i);
 
    } else if (head < end) {
      for (unsigned long long i = head, insert_idx = 0; i < end;
           ++i, ++insert_idx)
        *(ptr_data_new.get() + insert_idx) = *(ptr_data.get() + i);
    }
    head = 0;
    end = size;
    ptr_data = std::move(ptr_data_new);
    capacity = capacity_new;
  }
}
 
template <typename data_t>
data_t Queue<data_t>::pop_front() {
  data_t result;
  if (size != 0) {
    result = *(ptr_data.get() + head);
    head = (head + 1) % capacity;
    size--;
  }
  decrease_capacity();
  return result;
}
 
template <typename data_t>
std::string Queue<data_t>::to_string() {
  std::string result = "[";
  unsigned long long index = head;
  for (unsigned long long i = 0; i < size; i++) {
    result += std::to_string(*(ptr_data.get() + index));
    index = (index + 1) % capacity;
    if (i < size - 1) result += " ";
  }
  result += "]";
  return result;
}
 
void test_case() {
  Queue<value_t> que;
  value_t v;
  std::string res = "";
  que.push_back(65);
  que.push_back(66);
  que.push_back(67);
  std::cout << que.to_string() << "\n";
 
  v = que.pop_front();
  std::cout << v << " " << que.to_string() << "\n";
 
  que.push_back(68);
  std::cout << que.to_string() << "\n";
 
  v = que.pop_front();
  std::cout << v << " " << que.to_string() << "\n";
 
  v = que.pop_front();
  std::cout << v << " " << que.to_string() << "\n";
 
  que.push_back(69);
  std::cout << que.to_string() << "\n";
 
  que.push_back(69);
  std::cout << que.to_string() << "\n";
}
 
void cli_dialog() {
  long n_qry;
  value_t argument;
  std::string command, line, result = "";
  std::istringstream sstream;
  Queue<value_t> que;
 
  std::cin >> n_qry;
  std::cin.ignore();
  for (size_t i = 0; i < n_qry; ++i) {
    getline(std::cin, line);
    sstream = std::istringstream(line);
    if (line[0] == '+') {
      sstream >> command >> argument;
      que.push_back(argument);
    } else if (line[0] == '-') {
      result += (std::to_string(que.front()) + "\n");
      que.pop_front();
    }
  }
  std::cout << result;
}
 
bool random_bool(float threshold = 0.3) {
  return ((float)rand()) / RAND_MAX >= threshold;
}
 
template <typename data_t>
class Counter {
 private:
  data_t number = 0;
 
 public:
  data_t operator()() { return ++number; }
};
 
void stress_testing(long long n_trials = 2000) {
  Counter<value_t> counter;
  for (int i = 0; i < n_trials; ++i) {
    Queue<value_t> que_act;
    std::queue<value_t> que_exp;
    std::string hist = "";
    for (int j = 0; j < 12; ++j) {
      if (random_bool() and que_exp.size() > 0) {
        value_t act = que_act.front(), exp = que_exp.front();
        que_exp.pop();
        que_act.pop_front();
        hist += "-\n";
        if (exp != act) {
          std::cout << hist << "\n";
          std::cout << "act=" << act << " exp=" << exp << "\n";
          return;
        }
      } else {
        value_t v = counter();
        hist += ("+ " + std::to_string(v) + "\n");
        que_act.push_back(v);
        que_exp.push(v);
      }
    }
  }
}
 
int main() {
  // test_case();
  // stress_testing();
  cli_dialog();
}