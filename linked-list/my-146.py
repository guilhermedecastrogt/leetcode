class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.start, self.end = Node(0, 0), Node(0, 0)
        self.start.next = self.end
        self.end.prev = self.start
    
    def include(self, node):
        start, end = self.end.prev, self.end
        start.next, end.prev = node, node
        node.prev, node.next = start, end
        self.hashmap[node.key] = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        if node.key in self.hashmap:
            del self.hashmap[node.key]

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.include(node)
            return self.hashmap[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key, value)
        self.include(node)
        self.hashmap[key] = node

        if len(self.hashmap) > self.capacity:
            r = self.start.next
            self.remove(r)
            if r.key in self.hashmap:
                del self.hashmap[r.val]