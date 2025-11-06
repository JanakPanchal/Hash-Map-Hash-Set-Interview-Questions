"""
Problem: Single Number
Find the only element that appears once (others appear twice).
"""

def single_number_xor(nums):
    """
    Solution: Use XOR operation (a ^ a = 0, a ^ 0 = a)
    Time: O(n), Space: O(1)
    """
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_hash(nums):
    """
    Alternative: Use set to find unique number
    Time: O(n), Space: O(n)
    """
    return 2 * sum(set(nums)) - sum(nums)

# Test
if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(single_number_xor(nums))  # 4
    print(single_number_hash(nums))  # 4