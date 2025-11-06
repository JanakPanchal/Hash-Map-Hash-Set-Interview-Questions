"""
Problem: Find All Duplicates in an Array
Find all elements that appear twice (array values are 1..n).
"""

def find_duplicates_inplace(nums):
    """
    Solution: Use in-place marking (flip sign)
    Time: O(n), Space: O(1) excluding result
    """
    result = []
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        nums[idx] = -nums[idx]
    return result

def find_duplicates_hash(nums):
    """
    Alternative: Use hash map if can't modify array
    Time: O(n), Space: O(n)
    """
    count = {}
    result = []
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] == 2:
            result.append(num)
    return result

# Test
if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(find_duplicates_inplace(nums.copy()))  # [2, 3]
    print(find_duplicates_hash(nums))            # [2, 3]