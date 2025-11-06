"""
Problem: LFU Cache
Design Least Frequently Used cache with O(1) operations.
"""

class DLinkedNode:
    def __init__(self, key=0, val=0, freq=0):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_from_tail(self):
        if self.head.next == self.tail:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_list = {}
        self.min_freq = 0

    def get(self, key):
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._increase_freq(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._increase_freq(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                self._remove_lfu_node()

            new_node = DLinkedNode(key, value, 1)
            self.key_to_node[key] = new_node
            self.min_freq = 1

            if 1 not in self.freq_to_list:
                self.freq_to_list[1] = DLinkedList()
            self.freq_to_list[1].add_to_head(new_node)

    def _increase_freq(self, node):
        freq = node.freq
        self.freq_to_list[freq].remove_node(node)

        if self.min_freq == freq and self.freq_to_list[freq].head.next == self.freq_to_list[freq].tail:
            self.min_freq += 1

        node.freq += 1
        new_freq = node.freq

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DLinkedList()
        self.freq_to_list[new_freq].add_to_head(node)

    def _remove_lfu_node(self):
        node = self.freq_to_list[self.min_freq].remove_from_tail()
        if node:
            del self.key_to_node[node.key]

# Test
if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))    # 1
    cache.put(3, 3)        # evicts key 2
    print(cache.get(2))    # -1