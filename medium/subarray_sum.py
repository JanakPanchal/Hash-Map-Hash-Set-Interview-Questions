"""
Problem: Subarray Sum Equals K
Count the number of subarrays that sum to k.
"""

def subarray_sum(nums, k):
    """
    Solution: Prefix sum with frequency hash map
    Time: O(n), Space: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}  # prefix sum → frequency

    for num in nums:
        prefix_sum += num
        count += sum_freq.get(prefix_sum - k, 0)
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count

# Test
if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))      # 2
    print(subarray_sum([1, 2, 3], 3))      # 2
    print(subarray_sum([1, -1, 0], 0))     # 3