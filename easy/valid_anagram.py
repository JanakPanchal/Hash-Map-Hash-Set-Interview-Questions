"""
Problem: Valid Anagram
Check if two strings are anagrams of each other.
"""

def is_anagram(s, t):
    """
    Solution: Use hash map to count character frequencies
    Time: O(n), Space: O(k) where k = alphabet size
    """
    if len(s) != len(t):
        return False

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        char_count[char] = char_count.get(char, 0) - 1
        if char_count[char] < 0:
            return False

    return True

# Test
if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False