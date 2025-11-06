"""
Problem: First Missing Positive
Find smallest missing positive integer in O(n) time, O(1) space.
"""

def first_missing_positive_cyclic(nums):
    """
    Solution: Cyclic sort approach
    Time: O(n), Space: O(1)
    """
    n = len(nums)

    # Cyclic sort
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

def first_missing_positive_hash(nums):
    """
    Alternative: Use hash set (O(n) space)
    Time: O(n), Space: O(n)
    """
    nums_set = set(nums)
    i = 1
    while i in nums_set:
        i += 1
    return i

# Test
if __name__ == "__main__":
    nums = [3, 4, -1, 1]
    print(first_missing_positive_cyclic(nums.copy()))  # 2
    print(first_missing_positive_hash(nums))           # 2