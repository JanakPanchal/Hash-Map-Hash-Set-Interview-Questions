"""
Problem: Word Pattern
Check if a string follows a pattern (e.g., "abba" ↔ "dog cat cat dog").
"""

def word_pattern(pattern, s):
    """
    Solution: Bi-directional mapping with two hash maps
    Time: O(n), Space: O(k)
    """
    words = s.split()
    if len(pattern) != len(words):
        return False

    p_to_w = {}
    w_to_p = {}

    for p, w in zip(pattern, words):
        if p in p_to_w and p_to_w[p] != w:
            return False
        if w in w_to_p and w_to_p[w] != p:
            return False
        p_to_w[p] = w
        w_to_p[w] = p

    return True

# Test
if __name__ == "__main__":
    print(word_pattern("abba", "dog cat cat dog"))  # True
    print(word_pattern("abba", "dog cat cat fish"))  # False
    print(word_pattern("aaaa", "dog cat cat dog"))   # False