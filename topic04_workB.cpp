/**
B. Постфиксная запись
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.

Дано выражение в обратной польской записи. Определите его значение.

Входные данные
В единственной строке записано выражение в постфиксной записи, содержащее однозначные числа и операции +, -, *. Строка содержит не более 100 чисел и операций.

Выходные данные
Необходимо вывести значение записанного выражения. Гарантируется, что результат выражения, а также результаты всех промежуточных вычислений по модулю меньше 231.

Пример
входные данныеСкопировать
8 9 + 1 7 - *
выходные данныеСкопировать
-102

**/
#include <iostream>
#include <memory>
#include <sstream>
#include <string>
 
template <typename data_t>
class Stack {
 private:
  std::unique_ptr<data_t[]> ptr_data;
  size_t init_size, growth_factor, capacity, size = 0, min_capacity = 2;
 
 public:
  Stack(size_t init_size = 2, size_t growth_factor = 2);
  void push_back(data_t data);
  data_t back();
  void pop_back();
  std::string to_string();
  bool is_empty();
  void increase_capacity();
  void decrease_capacity();
};
 
template <typename data_t>
Stack<data_t>::Stack(size_t init_size_, size_t growth_factor_)
    : init_size(init_size_),
      growth_factor(growth_factor_),
      capacity(init_size) {
  data_t *p = new data_t[init_size_];
  ptr_data = std::unique_ptr<data_t[]>(p);
}
 
template <typename data_t>
void Stack<data_t>::increase_capacity() {
  if (size >= capacity) {
    size_t capacity_new = capacity * growth_factor;
    data_t *p = new data_t[capacity_new];
    std::unique_ptr<data_t[]> ptr_data_new = std::unique_ptr<data_t[]>(p);
    for (size_t i = 0; i < size; i++)
      *(ptr_data_new.get() + i) = *(ptr_data.get() + i);
    ptr_data = std::move(ptr_data_new);
    capacity = capacity_new;
  }
}
 
template <typename data_t>
void Stack<data_t>::push_back(data_t data) {
  increase_capacity();
  *(ptr_data.get() + size++) = data;
}
 
template <typename data_t>
data_t Stack<data_t>::back() {
  if (size > 0)
    return *(ptr_data.get() + size - 1);
  else
    throw "empty stack";
}
 
template <typename data_t>
void Stack<data_t>::decrease_capacity() {
  if (growth_factor * size < capacity and capacity > min_capacity) {
    size_t capacity_new = capacity / growth_factor;
    data_t *p = new data_t[capacity_new];
    std::unique_ptr<data_t[]> ptr_data_new = std::unique_ptr<data_t[]>(p);
    for (size_t i = 0; i < size; i++)
      *(ptr_data_new.get() + i) = *(ptr_data.get() + i);
    ptr_data = std::move(ptr_data_new);
    capacity = capacity_new;
  }
}
 
template <typename data_t>
void Stack<data_t>::pop_back() {
  if (size == 0) throw "pop_back: empty stack";
  size--;
  decrease_capacity();
}
 
template <typename data_t>
std::string Stack<data_t>::to_string() {
  std::string result = "[";
  for (size_t i = 0; i < size; i++) {
    result += std::to_string(*(ptr_data.get() + i));
    if (i < size - 1) result += " ";
  }
  result += "]";
  return result;
}
 
template <typename data_t>
bool Stack<data_t>::is_empty() {
  return size == 0;
}
 
void test_stack() {
  Stack<char> stack = Stack<char>();
  stack.push_back('a');
  stack.push_back('b');
  std::cout << stack.to_string() << "\n";
  stack.push_back('c');
  stack.push_back('d');
  std::cout << stack.to_string() << "\n";
  stack.push_back('e');
  stack.push_back('f');
  std::cout << stack.to_string() << "\n";
  stack.pop_back();
  std::cout << stack.to_string() << "\n";
  stack.pop_back();
  stack.pop_back();
  stack.pop_back();
  stack.pop_back();
  std::cout << stack.to_string() << "\n";
}
 
long long evaluate(long long left, char operation, long long right) {
  long long result;
  switch (operation) {
    case '+':
      result = left + right;
      break;
    case '-':
      result = left - right;
      break;
    case '*':
      result = left * right;
      break;
    case '/':
      result = left / right;
      break;
    default:
      std::string msg = "invalid operation: ";
      msg += operation;
      throw msg;
      break;
  }
  return result;
}
 
void cli_dialog() {
  std::string line;
  Stack<long long> numbers;
  getline(std::cin, line);
  for (char c : line) {
    if ('0' <= c and c <= '9') {
      numbers.push_back((long long)(c - '0'));
    } else if (c == '+' or c == '-' or c == '*') {
      long long left, right, result;
      right = numbers.back();
      numbers.pop_back();
      left = numbers.back();
      numbers.pop_back();
      result = evaluate(left, c, right);
      numbers.push_back(result);
    }
  }
  std::cout << numbers.back() << "\n";
}
 
int main() {
  // test_stack();
  cli_dialog();
  return 0;
}