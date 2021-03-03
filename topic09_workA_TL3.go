/*
A. Сбалансированное двоичное дерево поиска
ограничение по времени на тест2 секунды
ограничение по памяти на тест512 мегабайт
вводстандартный ввод
выводстандартный вывод
Реализуйте сбалансированное двоичное дерево поиска.

Входные данные
Входной файл содержит описание операций с деревом, их количество не превышает 105. В каждой строке находится одна из следующих операций:

insert 𝑥 — добавить в дерево ключ 𝑥. Если ключ 𝑥 есть в дереве, то ничего делать не надо;
delete 𝑥 — удалить из дерева ключ 𝑥. Если ключа 𝑥 в дереве нет, то ничего делать не надо;
exists 𝑥 — если ключ 𝑥 есть в дереве выведите «true», если нет «false»;
next 𝑥 — выведите минимальный элемент в дереве, строго больший 𝑥, или «none» если такого нет;
prev 𝑥 — выведите максимальный элемент в дереве, строго меньший 𝑥, или «none» если такого нет.
В дерево помещаются и извлекаются только целые числа, не превышающие по модулю 109.
Выходные данные
Выведите последовательно результат выполнения всех операций exists, next, prev. Следуйте формату выходного файла из примера.

Пример
входные данныеСкопировать
insert 2
insert 5
insert 3
exists 2
exists 4
next 4
prev 4
delete 5
next 4
prev 4
выходные данныеСкопировать
true
false
5
3
none
3
*/

package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	x     int
	y     int
	left  *Node
	right *Node
	// parent *Node
}

type Pair struct {
	level int
	node  *Node
}

// type is_good func(*Node) bool

func to_string(node *Node) string {
	var result string = ""
	buff := list.New()
	buff.PushBack(Pair{level: 0, node: node})
	for buff.Len() > 0 {
		var curr Pair = buff.Back().Value.(Pair)
		result += strings.Repeat(" ", curr.level) + "{x:" + strconv.Itoa(curr.node.x) + " y:" + strconv.Itoa(curr.node.y) + "}\n"
		buff.Remove(buff.Back())
		if node.right != nil {
			buff.PushBack(Pair{level: curr.level + 1, node: node.right})
		}
		if node.left != nil {
			buff.PushBack(Pair{level: curr.level + 1, node: node.left})
		}
	}
	return result
}

func merge(left *Node, right *Node) *Node {
	if right == nil {
		return left
	}
	if left == nil {
		return right
	}
	if left.y > right.y {
		left.right = merge(left.right, right)
		return left
	} else {
		right.left = merge(left, right.left)
		return right
	}
}

func split(node *Node, x int) (*Node, *Node) {
	if node == nil {
		return nil, nil
	} else if node.x > x {
		node_left, node_right := split(node.left, x)
		node.left = node_right
		return node_left, node
	} else {
		node_left, node_right := split(node.right, x)
		node.right = node_left
		return node, node_right
	}
}

// func insert(node *Node, x int, y int) *Node {
// 	node_new := Node{x, y, nil, nil}
// 	if node == nil {
// 		return &node_new
// 	} else {
// 		left, right := split(node, x)
// 		left = merge(left, &node_new)
// 		return merge(left, right)
// 	}
// }

func insert(node *Node, x int, y int) *Node {
	node_new := Node{x, y, nil, nil}
	if node == nil {
		return &node_new
	} else {
		var parent *Node = nil
		var curr *Node = node
		for curr != nil {
			if curr.y < y {
				break
			}
			parent = curr
			if x <= curr.x {
				curr = curr.left
			} else {
				curr = curr.right
			}
		}
		left, right := split(curr, x)
		node_new.left = left
		node_new.right = right
		if parent == nil {
			return &node_new
		} else {
			if x <= parent.x {
				parent.left = &node_new
			} else {
				parent.right = &node_new
			}
		}

		// curr = &node_new
		// if curr == nil {
		// 	if x <= parent.x {
		// 		parent.left = &node_new
		// 	} else {
		// 		parent.right = &node_new
		// 	}
		// 	// curr = &node_new
		// } else {
		// 	left, right := split(curr, x)
		// 	node_new.left = left
		// 	node_new.right = right
		// 	curr = &node_new

		// 	// curr.x = x
		// 	// curr.y = y
		// 	// curr.left = left
		// 	// curr.right = right
		// }
	}
	return node
}

func remove(node *Node, x int) *Node {
	left, right := split(node, x)
	left_2, _ := split(left, x-1)
	return merge(left_2, right)
}

func exists(node *Node, x int) bool {
	var result bool = false
	for node != nil {
		if node.x == x {
			result = true
			break
		}
		if x < node.x {
			node = node.left
		} else if x > node.x {
			node = node.right
		}
	}
	return result
}

func prev(node *Node, x int) *Node {
	var is_initialised bool = false
	var x_max int
	var node_best *Node = nil
	for node != nil {
		if node.x < x {
			if !is_initialised || node.x > x_max {
				x_max = node.x
				node_best = node
				is_initialised = true
			}
		}
		if x < node.x {
			node = node.left
		} else if x > node.x {
			node = node.right
		}
	}
	return node_best
}

func next(node *Node, x int) *Node {
	var is_initialised bool = false
	var x_min int
	var node_best *Node = nil
	for node != nil {
		if node.x > x {
			if !is_initialised || node.x < x_min {
				x_min = node.x
				node_best = node
				is_initialised = true
			}
		}
		if x < node.x {
			node = node.left
		} else if x > node.x {
			node = node.right
		}
	}
	return node_best
}

func cli_dialog() {
	const MAX_Y = 1000000
	var root *Node = nil
	reader := bufio.NewReader(os.Stdin)
	var is_exit bool = false
	var next_y int = 0
	for !is_exit {
		command, err := reader.ReadString('\n')
		if err == nil {
			if strings.HasPrefix(command, "insert") {
				arg, _ := strconv.Atoi(strings.Fields(command)[1])
				root = insert(root, arg, next_y)
				next_y++
			} else if strings.HasPrefix(command, "delete") {
				arg, _ := strconv.Atoi(strings.Fields(command)[1])
				root = remove(root, arg)
			} else if strings.HasPrefix(command, "exists") {
				arg, _ := strconv.Atoi(strings.Fields(command)[1])
				fmt.Println(strconv.FormatBool(exists(root, arg)))
			} else if strings.HasPrefix(command, "next") {
				arg, _ := strconv.Atoi(strings.Fields(command)[1])
				res := next(root, arg)
				if res != nil {
					fmt.Println(res.x)
				} else {
					fmt.Println("none")
				}
			} else if strings.HasPrefix(command, "prev") {
				arg, _ := strconv.Atoi(strings.Fields(command)[1])
				res := prev(root, arg)
				if res != nil {
					fmt.Println(res.x)
				} else {
					fmt.Println("none")
				}
			}
		} else {
			is_exit = true
		}
	}

}

func test_case() {
	const MAX_Y = 1000000
	var root *Node = nil
	var next_y int = 0
	root = insert(root, 2, next_y)
	next_y++
	root = insert(root, 5, next_y)
	next_y++
	root = insert(root, 3, next_y)
	next_y++
	fmt.Println(strconv.FormatBool(exists(root, 2)))
	fmt.Println(strconv.FormatBool(exists(root, 4)))
	fmt.Println(next(root, 4))
	fmt.Println(prev(root, 4))
	root = remove(root, 5)
	fmt.Println(next(root, 4))
	fmt.Println(prev(root, 4))
}

func main() {
	// test_case()
	cli_dialog()
}
