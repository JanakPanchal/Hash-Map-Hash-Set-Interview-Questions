"""
Problem: Contains Duplicate
Return True if any value appears at least twice in the array.
"""

def contains_duplicate(nums):
    """
    Solution: Use set to track seen elements
    Time: O(n), Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Alternative one-liner
def contains_duplicate_alt(nums):
    return len(nums) != len(set(nums))

# Test
if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))  # True
    print(contains_duplicate([1, 2, 3, 4]))  # False