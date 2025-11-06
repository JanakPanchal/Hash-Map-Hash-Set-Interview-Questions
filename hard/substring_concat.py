"""
Problem: Substring with Concatenation of All Words
Find starting indices of substrings containing all words exactly once.
"""

from collections import Counter

def find_substring(s, words):
    """
    Solution: Use sliding window with word frequency map
    Time: O(n * m * k), Space: O(m)
    """
    if not words or not s:
        return []

    word_len = len(words[0])
    total_len = word_len * len(words)
    word_count = Counter(words)
    result = []

    for i in range(len(s) - total_len + 1):
        seen = Counter()
        for j in range(i, i + total_len, word_len):
            word = s[j:j + word_len]
            if word not in word_count:
                break
            seen[word] += 1
            if seen[word] > word_count[word]:
                break
        else:
            result.append(i)

    return result

# Test
if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(find_substring(s, words))  # [0, 9]