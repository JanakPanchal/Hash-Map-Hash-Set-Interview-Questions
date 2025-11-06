"""
Problem: Intersection of Two Arrays
Return unique elements common to both arrays.
"""

def intersection(nums1, nums2):
    """
    Solution: Use set intersection operation
    Time: O(n + m), Space: O(min(n, m))
    """
    return list(set(nums1) & set(nums2))

# Alternative with manual set
def intersection_manual(nums1, nums2):
    set1 = set(nums1)
    result = set()
    for num in nums2:
        if num in set1:
            result.add(num)
    return list(result)

# Test
if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))  # [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4]