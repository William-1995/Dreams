package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"time"
)

const MaxLevel = 32
const Probability = 0.25 // 基于时间与空间综合 best practice 值, 越上层概率越小

/*
	Reference this blog to implement a skip list:
		https://xguox.me/go-skip-list.html/
 */
func randLevel() (level int) {
	rand.Seed(time.Now().UnixNano())
	for level = 1; rand.Float32() < Probability && level < MaxLevel; level++ {
	}
	return
}

type node struct {
	forward []*node
	key     int
	value 	string
}

type skipMap struct {
	head  *node
	level int
}

func newNode(key int,value string, level int) *node {
	return &node{key: key, forward: make([]*node, level), value: value}
}

func newskipMap() *skipMap {
	return &skipMap{head: newNode(0,"", MaxLevel), level: 1}
}

func (s *skipMap) insert(key int, value string) {
	current := s.head
	update := make([]*node, MaxLevel)

	// 找到要插入节点的前驱节点
	for i := s.level - 1; i >= 0; i-- {
		for current.forward[i] != nil && current.forward[i].key < key {
			current = current.forward[i] // 指针往前推进
		}
		update[i] = current
	}


	level := randLevel()
	// 更新level 如果随机生成的level 大于当前的最大的level
	if level > s.level {
		// 新节点层数大于跳表当前层数时候, 现有层数 + 1 的 head 指向新节点
		for i := s.level; i < level; i++ {
			update[i] = s.head
		}
		s.level = level
	}

	node := newNode(key,value,level)
	// 调整指针位置, 即将新插入的节点与其前驱及后继节点相连
	for i := 0; i < level; i++ {
		node.forward[i] = update[i].forward[i]
		update[i].forward[i] = node
	}
}

func (s *skipMap) delete(key int) {
	current := s.head
	for i := s.level - 1; i >= 0; i-- {
		for current.forward[i] != nil {
			// 将被删除的节点设置成nil, 并将被删除节点的前驱与被删除节点的后继节点相连
			if current.forward[i].key == key {
				tmp := current.forward[i]
				current.forward[i] = tmp.forward[i]
				tmp.forward[i] = nil
			} else if current.forward[i].key > key {
				break
			} else {
				current = current.forward[i]
			}
		}
	}

}

func (s *skipMap) search(key int) *node {
	current := s.head
	for i := s.level - 1; i >= 0; i-- {
		for (current.forward[i].key < key) {
			current = current.forward[i]
		}
	}

	if current.forward[0].key == key {
		return current.forward[0]
	}

	return nil;
}

func (s *skipMap) print() {
	for i := s.level - 1; i >= 0; i-- {
		current := s.head
		for current.forward[i] != nil {
			fmt.Printf("%d ", current.forward[i].key)
			current = current.forward[i]
		}
		fmt.Printf("***************** Level %d \n", i+1)
	}
}

func main() {
	list := newskipMap()
	ran := [11] int {5,8,9,6,3,1,4,7,2,0,2}
	for i := 0; i < 10; i++ {
		list.insert(ran[i], strconv.Itoa(ran[i]) + "map value");
	}
	list.print()

	list.delete(6)
	list.print()

	fmt.Println(list.search(2).value)
}
