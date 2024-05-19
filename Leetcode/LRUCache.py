# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prevs = self.right.prev
        prevs.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prevs

    def remove(self, node):
        prevs = node.prev
        nexts = node.next
        prevs.next = nexts
        nexts.prev = prevs

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if self.cap < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
