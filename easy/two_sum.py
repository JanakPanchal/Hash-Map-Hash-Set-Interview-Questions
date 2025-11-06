"""
Problem: Two Sum
Given an array of integers nums and an integer target, return indices of two numbers that add up to target.
"""

def two_sum(nums, target):
    """
    Solution: Use hash map to store seen numbers and their indices
    Time: O(n), Space: O(n)
    """
    seen = {}  # number → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))       # [1, 2]