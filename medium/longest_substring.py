"""
Problem: Longest Substring Without Repeating Characters
Find length of longest substring without repeating characters.
"""

def length_of_longest_substring(s):
    """
    Solution: Sliding window with hash map tracking last index
    Time: O(n), Space: O(k)
    """
    char_map = {}
    max_len = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        max_len = max(max_len, i - start + 1)

    return max_len

# Test
if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
    print(length_of_longest_substring("bbbbb"))     # 1 ("b")
    print(length_of_longest_substring("pwwkew"))    # 3 ("wke")