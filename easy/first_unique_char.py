"""
Problem: First Unique Character
Find the index of first non-repeating character in a string.
"""

def first_unique_char(s):
    """
    Solution: Count frequencies then find first char with count = 1
    Time: O(n), Space: O(k)
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1

# Test
if __name__ == "__main__":
    print(first_unique_char("leetcode"))  # 0
    print(first_unique_char("loveleetcode"))  # 2
    print(first_unique_char("aabb"))  # -1