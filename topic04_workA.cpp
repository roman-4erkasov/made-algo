/**
A. Минимум на стеке
ограничение по времени на тест2 секунды
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Вам требуется реализовать структуру данных, выполняющую следующие операции:

Добавить элемент 𝑥 в конец структуры.
Удалить последний элемент из структуры.
Выдать минимальный элемент в структуре.
Входные данные
В первой строке входного файла задано одно целое число 𝑛 — количество операций (1≤𝑛≤106). В следующих 𝑛 строках заданы сами операции. В 𝑖–ой строке число 𝑡𝑖 — тип операции (1, если операция добавления. 2, если операция удаления. 3, если операция минимума). Если задана операция добавления, то через пробел записано целое число 𝑥 — элемент, который следует добавить в структуру (−109≤𝑥≤109). Гарантируется, что перед каждой операцией удаления или нахождения минимума структура не пуста.

Выходные данные
Для каждой операции нахождения минимума выведите одно число — минимальный элемент в структуре. Ответы разделяйте переводом строки.

Пример
входные данныеСкопировать
8
1 2
1 3
1 -3
3
2
3
2
3
выходные данныеСкопировать
-3
2
2

**/
#include <cassert>
#include <iostream>
#include <memory>
#include <sstream>
#include <string>
 
typedef long long value_t;
 
template <typename data_t>
struct Node : std::enable_shared_from_this<Node<data_t> > {
 public:
  data_t data;
  data_t prev_min;
  bool is_first;
  std::shared_ptr<Node<data_t> > next;
  std::weak_ptr<Node<data_t> > prev;
  std::string to_string();
  data_t get_min();
};
 
template <typename data_t>
std::string Node<data_t>::to_string() {
  std::string result = std::to_string(this->data);
  return result;
}
 
template <typename data_t>
data_t Node<data_t>::get_min() {
  return (is_first or data < prev_min) ? data : prev_min;
}
 
void test_node() {
  Node<value_t> *n1 = new Node<value_t>(), *n2 = new Node<value_t>(),
                *n3 = new Node<value_t>();
  std::shared_ptr<Node<value_t> > ptr_n1(n1), ptr_n2(n2), ptr_n3(n3);
 
  ptr_n1->data = 1;
  ptr_n2->data = 2;
  ptr_n3->data = 3;
 
  ptr_n1->next = ptr_n2;
  ptr_n2->prev = ptr_n1;
 
  ptr_n2->next = ptr_n3;
  ptr_n3->prev = ptr_n2;
 
  assert(ptr_n1->data == 1);
  assert(ptr_n1->next == ptr_n2);
  assert(ptr_n1->prev.expired());
  assert(n1->prev.lock() == nullptr);
  assert(ptr_n1->next->data == 2);
  assert(ptr_n1->to_string() == "1");
 
  assert(ptr_n2->data == 2);
  assert(ptr_n2->prev.lock() == ptr_n1);
  assert(ptr_n2->next == ptr_n3);
  assert(ptr_n2->prev.lock()->data == 1);
  assert(ptr_n2->next->data == 3);
  assert(ptr_n2->to_string() == "2");
 
  assert(ptr_n3->data == 3);
  assert(ptr_n3->prev.lock() == ptr_n2);
  assert(ptr_n3->next == nullptr);
  assert(ptr_n3->prev.lock()->data == 2);
  assert(ptr_n3->to_string() == "3");
  std::cout << "test_node: ok (1/2)\n";
 
  ptr_n2->data = 20;
  assert(ptr_n1->next->data == 20);
  assert(ptr_n3->prev.lock()->data == 20);
  std::cout << "test_node: ok (2/2)\n";
}
 
template <typename data_t>
class MinStack {
 private:
  std::shared_ptr<Node<data_t> > head, tail;
  long long length = 0;
  void init(data_t data);
 
 public:
  std::string to_string();
  void push_back(data_t data);
  data_t back();
  void pop_back();
  data_t get_min();
};
 
template <typename data_t>
void MinStack<data_t>::init(data_t data) {
  Node<data_t> *node = new Node<data_t>();
  node->data = data;
  node->is_first = true;
  tail = std::shared_ptr<Node<data_t> >(node);
  head = tail;
}
 
template <typename data_t>
void MinStack<data_t>::push_back(data_t data) {
  if (tail == nullptr)
    init(data);
  else {
    Node<data_t> *node = new Node<data_t>();
    node->data = data;
    std::shared_ptr<Node<data_t> > ptr_node(node), tmp = tail;
    tail = ptr_node;
    ptr_node->prev = tmp;
    tmp->next = ptr_node;
 
    tail->prev_min = tail->prev.lock()->get_min();
  }
  length++;
}
 
template <typename data_t>
data_t MinStack<data_t>::back() {
  return tail->data;
}
 
template <typename data_t>
void MinStack<data_t>::pop_back() {
  if (length == 1) {
    head = nullptr;
    tail = nullptr;
    length--;
  } else if (length > 1) {
    tail = tail->prev.lock();
    tail->next = nullptr;
    length--;
  }
}
 
template <typename data_t>
std::string MinStack<data_t>::to_string() {
  std::string result = "[";
  std::shared_ptr<Node<data_t> > curr = head;
  while (curr != nullptr) {
    result += curr->to_string();
    if (curr->next != nullptr) result += " ";
    curr = curr->next;
  }
  result += "]";
  return result;
}
 
template <typename data_t>
data_t MinStack<data_t>::get_min() {
  return tail->get_min();
}
 
void test_minstack() {
  MinStack<value_t> stack;
  stack.push_back(10);
  stack.push_back(20);
  stack.push_back(3);
  assert(stack.to_string() == "[10 20 3]");
  assert(stack.get_min() == 3);
  assert(stack.back() == 3);
  std::cout << "test_list: ok (1/2)\n";
  stack.pop_back();
  assert(stack.to_string() == "[10 20]");
  assert(stack.get_min() == 10);
  assert(stack.back() == 20);
  std::cout << "test_list: ok (2/2)\n";
}
 
void cli_dialog(bool verbose = false) {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);
 
  MinStack<value_t> stack;
  std::istringstream sstream;
  long long n_qry = 0;
  std::string command, result = "";
  std::cin >> n_qry;
  std::cin.ignore();
  if (verbose) std::cout << "nqry=" << n_qry << "\n";
  for (long long i = 0; i < n_qry; i++) {
    getline(std::cin, command);
    if (verbose) std::cout << "cmd=" << command << "\n";
    if (command[0] == '1') {
      sstream = std::istringstream(command);
      short cmd;
      value_t value;
      sstream >> cmd >> value;
      stack.push_back(value);
    } else if (command[0] == '2') {
      stack.pop_back();
    } else if (command[0] == '3') {
      result += (std::to_string(stack.get_min()) + "\n");
    }
  }
  std::cout << result;
}
 
int main() {
  // test_node();
  // test_minstack();
  cli_dialog();
  return 0;
}