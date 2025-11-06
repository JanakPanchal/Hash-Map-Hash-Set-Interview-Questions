import pytest
import sys
import os

sys.path.append(os.path.abspath('.'))

from medium.group_anagrams import group_anagrams
from medium.top_k_frequent import top_k_frequent_counter, top_k_frequent_bucket
from medium.longest_substring import length_of_longest_substring
from medium.word_pattern import word_pattern
from medium.subarray_sum import subarray_sum
from medium.find_all_duplicates import find_duplicates_hash


class TestMedium:
    def test_group_anagrams(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = group_anagrams(strs)
        assert len(result) == 3

    def test_top_k_frequent(self):
        nums = [1, 1, 1, 2, 2, 3]
        assert sorted(top_k_frequent_counter(nums, 2)) == [1, 2]
        assert sorted(top_k_frequent_bucket(nums, 2)) == [1, 2]

    def test_longest_substring(self):
        assert length_of_longest_substring("abcabcbb") == 3
        assert length_of_longest_substring("bbbbb") == 1
        assert length_of_longest_substring("pwwkew") == 3

    def test_word_pattern(self):
        assert word_pattern("abba", "dog cat cat dog") == True
        assert word_pattern("abba", "dog cat cat fish") == False
        assert word_pattern("aaaa", "dog cat cat dog") == False

    def test_subarray_sum(self):
        assert subarray_sum([1, 1, 1], 2) == 2
        assert subarray_sum([1, 2, 3], 3) == 2

    def test_find_all_duplicates(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        assert sorted(find_duplicates_hash(nums)) == [2, 3]