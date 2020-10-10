package main

import (
	"fmt"
	"math"
)

type BloomFilter struct {
	len       int64   // Filter len.
	arr       []int64 // Filter array.
	count     int64   // Insert element count.
	rate      float64 // False alarm rate.
	hashCount int     // The count of hash functions.
}

func main() {
	bf := NewBloomFilter(0.0001,100)
	fmt.Println(bf)
	bf.set([]byte("willl"))
	bf.set([]byte("liu"))
	bf.set([]byte("xu"))

	fmt.Println(bf.check([]byte("xu")))

	fmt.Println(bf)
}

func NewBloomFilter(rate float64, size int64) *BloomFilter {
	m, k := getFilterParam(rate, size)

	return &BloomFilter{
		len:       m,
		arr:       make([]int64, m),
		count:     size,
		rate:      rate,
		hashCount: k,
	}
}

func getFilterParam(rate float64, size int64) (int64, int) {
	m := -1 * math.Log(rate) * float64((size)) / (math.Ln2 * math.Ln2)
	k := m * math.Ln2 / float64(size)
	return int64(m), int(k)
}

func (bf *BloomFilter) set(data []byte) {
	for i := 0; i < bf.hashCount; i++ {
		index := bf.hashFun(data, i)
		bf.arr[index] = 1
	}
}

func (bf *BloomFilter) check(data []byte) bool {
	for i := 0; i < bf.hashCount; i++ {
		index := bf.hashFun(data, i)
		if bf.arr[index] == 0 {
			return false
		}
	}
	return true
}

func (bf *BloomFilter) hashFun(data []byte, count int) int64 {
	hash := int64(5381)
	for i := 0; i < len(data); i++ {
		hash = hash*33 + int64(data[i]) + int64(count)
	}
	res := hash % (bf.len - 1)
	return int64(math.Abs(float64(res)))
}
