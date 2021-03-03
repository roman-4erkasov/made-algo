#include <math.h>
 
#include <iostream>
#include <list>
#include <memory>
#include <sstream>
#include <string>
#include <vector>
 
class StringMap {
 private:
  const unsigned long long BASE = 31;
  const unsigned long long PRIME = 10007;
  std::vector<std::list<std::pair<std::string, std::string> > > data;
 
 public:
  StringMap();
  unsigned long long poly_hash(std::string string);
  void put(std::string key, std::string value);
  void del(std::string key);
  std::string get(std::string key);
};
 
unsigned long long StringMap::poly_hash(std::string string) {
  unsigned long long result = 0;
  unsigned long long power = 1;
  for (auto &&c : string) {
    result = (result + (c - 'a' + 1) * power) % PRIME;
    power = (power * BASE) % PRIME;
  }
  return result;
}
 
StringMap::StringMap() {
  data = std::vector<std::list<std::pair<std::string, std::string> > >(PRIME);
}
 
void StringMap::put(std::string key, std::string value) {
  unsigned long long index = poly_hash(key);
  bool found = false;
  std::list<std::pair<std::string, std::string> >::iterator it;
  for (it = data[index].begin(); it != data[index].end(); ++it) {
    if (it->first == key) {
      found = true;
      it->second = value;
      break;
    }
  }
  if (not found) data[index].push_back(std::make_pair(key, value));
}
 
void StringMap::del(std::string key) {
  unsigned long long index = poly_hash(key);
  std::list<std::pair<std::string, std::string> >::iterator it;
  for (it = data[index].begin(); it != data[index].end(); ++it) {
    if (it->first == key) {
      data[index].erase(it);
      break;
    }
  }
}
 
std::string StringMap::get(std::string key) {
  unsigned long long index = poly_hash(key);
  std::string value = "none";
  std::list<std::pair<std::string, std::string> >::iterator it;
  for (it = data[index].begin(); it != data[index].end(); ++it) {
    if (it->first == key) {
      value = it->second;
      break;
    }
  }
  return value;
}
 
void cli_dialog() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);
 
  std::string line, command, result = "";
  std::string argument1, argument2;
  StringMap map;
  std::istringstream sstream;
  while (getline(std::cin, line)) {
    if (line.rfind("put", 0) == 0) {
      sstream = std::istringstream(line);
      sstream >> command >> argument1 >> argument2;
      map.put(argument1, argument2);
    } else if (line.rfind("delete", 0) == 0) {
      sstream = std::istringstream(line);
      sstream >> command >> argument1;
      map.del(argument1);
    } else if (line.rfind("get", 0) == 0) {
      sstream = std::istringstream(line);
      sstream >> command >> argument1;
      std::cout << map.get(argument1) << "\n";
    }
  }
}
 
int main() { cli_dialog(); }