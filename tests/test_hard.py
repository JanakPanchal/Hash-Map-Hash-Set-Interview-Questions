import pytest
import sys
import os

sys.path.append(os.path.abspath('.'))

from hard.lru_cache import LRUCache
from hard.lfu_cache import LFUCache
from hard.all_one_data_structure import AllOne
from hard.design_twitter import Twitter
from hard.first_missing_positive import first_missing_positive_cyclic, first_missing_positive_hash


class TestHard:
    def test_lru_cache(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)  # evicts key 2
        assert cache.get(2) == -1
        cache.put(4, 4)  # evicts key 1
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4

    def test_lfu_cache(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)  # evicts key 2
        assert cache.get(2) == -1

    def test_all_one(self):
        obj = AllOne()
        obj.inc("a")
        obj.inc("b")
        obj.inc("a")
        assert obj.getMaxKey() == "a"
        assert obj.getMinKey() == "b"

    def test_twitter(self):
        twitter = Twitter()
        twitter.postTweet(1, 5)
        assert 5 in twitter.getNewsFeed(1)

    def test_first_missing_positive(self):
        nums = [3, 4, -1, 1]
        assert first_missing_positive_cyclic(nums.copy()) == 2
        assert first_missing_positive_hash(nums) == 2