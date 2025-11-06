"""
Problem: All O`one Data Structure
Supports inc/dec/getMaxKey/getMinKey in O(1).
"""

class DLinkedNode:
    def __init__(self):
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}  # key → node with that frequency
        self.node_to_freq = {}  # node → frequency (optional)

    def inc(self, key):
        """
        Increase key count by 1
        Time: O(1)
        """
        if key not in self.key_to_node:
            # Add to first node (freq = 1)
            if self.head.next == self.tail or self.head.next.keys != {None}:
                new_node = DLinkedNode()
                new_node.keys = {key}
                new_node.freq = 1
                self._add_after(self.head, new_node)
                self.key_to_node[key] = new_node
            else:
                node = self.head.next
                node.keys.add(key)
                self.key_to_node[key] = node
        else:
            node = self.key_to_node[key]
            freq = self._get_freq(node)
            node.keys.remove(key)

            # Create or find next node (freq + 1)
            if node.next == self.tail or self._get_freq(node.next) != freq + 1:
                new_node = DLinkedNode()
                new_node.keys = {key}
                new_node.freq = freq + 1
                self._add_after(node, new_node)
                self.key_to_node[key] = new_node
            else:
                node.next.keys.add(key)
                self.key_to_node[key] = node.next

            if not node.keys:
                self._remove_node(node)

    def dec(self, key):
        """
        Decrease key count by 1
        Time: O(1)
        """
        if key not in self.key_to_node:
            return

        node = self.key_to_node[key]
        freq = self._get_freq(node)
        node.keys.remove(key)

        if freq > 1:
            # Create or find prev node (freq - 1)
            if node.prev == self.head or self._get_freq(node.prev) != freq - 1:
                new_node = DLinkedNode()
                new_node.keys = {key}
                new_node.freq = freq - 1
                self._add_after(node.prev, new_node)
                self.key_to_node[key] = new_node
            else:
                node.prev.keys.add(key)
                self.key_to_node[key] = node.prev
        else:
            del self.key_to_node[key]

        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self):
        """
        Return one key with max frequency
        Time: O(1)
        """
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        Return one key with min frequency
        Time: O(1)
        """
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

    def _add_after(self, prev, node):
        node.prev = prev
        node.next = prev.next
        prev.next.prev = node
        prev.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _get_freq(self, node):
        # Helper to get frequency from node
        return getattr(node, 'freq', 0)

# Test
if __name__ == "__main__":
    obj = AllOne()
    obj.inc("a")
    obj.inc("b")
    obj.inc("a")
    print(obj.getMaxKey())  # "a"
    print(obj.getMinKey())  # "b"