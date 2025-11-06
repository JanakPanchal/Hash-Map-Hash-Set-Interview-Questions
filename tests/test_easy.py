import pytest
import sys
import os

sys.path.append(os.path.abspath('.'))

from easy.two_sum import two_sum
from easy.contains_duplicate import contains_duplicate
from easy.valid_anagram import is_anagram
from easy.single_number import single_number_xor, single_number_hash
from easy.intersection import intersection
from easy.first_unique_char import first_unique_char


class TestEasy:
    def test_two_sum(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]
        assert two_sum([3, 2, 4], 6) == [1, 2]
        assert two_sum([3, 3], 6) == [0, 1]

    def test_contains_duplicate(self):
        assert contains_duplicate([1, 2, 3, 1]) == True
        assert contains_duplicate([1, 2, 3, 4]) == False
        assert contains_duplicate([]) == False

    def test_valid_anagram(self):
        assert is_anagram("anagram", "nagaram") == True
        assert is_anagram("rat", "car") == False
        assert is_anagram("a", "ab") == False

    def test_single_number(self):
        nums = [4, 1, 2, 1, 2]
        assert single_number_xor(nums) == 4
        assert single_number_hash(nums) == 4

    def test_intersection(self):
        assert sorted(intersection([1, 2, 2, 1], [2, 2])) == [2]
        assert sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]

    def test_first_unique_char(self):
        assert first_unique_char("leetcode") == 0
        assert first_unique_char("loveleetcode") == 2
        assert first_unique_char("aabb") == -1