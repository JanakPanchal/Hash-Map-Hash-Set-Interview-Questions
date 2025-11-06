"""
Problem: Top K Frequent Elements
Return the k most frequent elements.
"""

from collections import Counter

def top_k_frequent_counter(nums, k):
    """
    Solution: Use Counter.most_common()
    Time: O(n log k), Space: O(n)
    """
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]

def top_k_frequent_bucket(nums, k):
    """
    Alternative: Use bucket sort for O(n) time
    Time: O(n), Space: O(n)
    """
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Bucket sort: index = frequency
    freq = [[] for _ in range(len(nums) + 1)]
    for num, c in count.items():
        freq[c].append(num)

    # Collect top k elements from highest frequency
    result = []
    for i in range(len(freq) - 1, 0, -1):
        if freq[i]:
            result.extend(freq[i])
            if len(result) >= k:
                return result[:k]

    return result

# Test
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent_counter(nums, k))  # [1, 2]
    print(top_k_frequent_bucket(nums, k))   # [1, 2]