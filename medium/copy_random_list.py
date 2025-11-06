"""
Problem: Copy List with Random Pointer
Deep copy a linked list with random pointers.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

def copy_random_list(head):
    """
    Solution: Use hash map to store old→new node mapping
    Time: O(n), Space: O(n)
    """
    if not head:
        return None

    old_to_new = {}

    # First pass: create all new nodes
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Second pass: assign next and random pointers
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]

# Test
if __name__ == "__main__":
    # Create list: 1→2→3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node1.random = node3
    node2.random = node1
    node3.random = node2

    copied = copy_random_list(node1)
    print(copied.val)  # 1