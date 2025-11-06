"""
Problem: Group Anagrams
Group all anagrams together from a list of strings.
"""

from collections import defaultdict

def group_anagrams(strs):
    """
    Solution: Use sorted string as key in hash map
    Time: O(n * k log k), Space: O(n * k)
    """
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# Alternative: Use character count as key
def group_anagrams_alt(strs):
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        groups[key].append(s)
    return list(groups.values())

# Test
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]