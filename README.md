# 🎯 Hash Map & Hash Set Interview Questions

A comprehensive collection of algorithm problems and solutions using hash-based data structures.

## 📚 Table of Contents

### Easy (6 problems)
| Problem | Solution | Time | Space |
|---------|----------|------|-------|
| [Two Sum](./easy/two_sum.py) | Python | O(n) | O(n) |
| [Contains Duplicate](./easy/contains_duplicate.py) | Python | O(n) | O(n) |
| [Valid Anagram](./easy/valid_anagram.py) | Python | O(n) | O(k) |
| [Single Number](./easy/single_number.py) | Python | O(n) | O(1) |
| [Intersection of Two Arrays](./easy/intersection.py) | Python | O(n+m) | O(min(n,m)) |
| [First Unique Character](./easy/first_unique_char.py) | Python | O(n) | O(k) |

### Medium (8 problems)
| Problem | Solution | Key Concept |
|---------|----------|-------------|
| [Group Anagrams](./medium/group_anagrams.py) | Python | Frequency Encoding |
| [Top K Frequent Elements](./medium/top_k_frequent.py) | Python | Bucket Sort + Hash |
| [Longest Substring Without Repeating Characters](./medium/longest_substring.py) | Python | Sliding Window |
| [Word Pattern](./medium/word_pattern.py) | Python | Bi-directional Mapping |
| [Subarray Sum Equals K](./medium/subarray_sum.py) | Python | Prefix Sum |
| [Find All Duplicates](./medium/find_all_duplicates.py) | Python | In-place Hashing |
| [Copy List with Random Pointer](./medium/copy_random_list.py) | Python | Old→New Mapping |
| [Logger Rate Limiter](./medium/logger_rate_limiter.py) | Python | Timestamp Cache |

### Hard (6 problems)
| Problem | Solution | Challenge |
|---------|----------|-----------|
| [LRU Cache](./hard/lru_cache.py) | Python | O(1) Operations |
| [LFU Cache](./hard/lfu_cache.py) | Python | Frequency Tracking |
| [All O`one Data Structure](./hard/all_one_data_structure.py) | Python | Max/Min in O(1) |
| [Design Twitter](./hard/design_twitter.py) | Python | Feed Generation |
| [Substring with Concatenation](./hard/substring_concat.py) | Python | Word Pattern Matching |
| [First Missing Positive](./hard/first_missing_positive.py) | Python | O(1) Space |

## 🔑 Key Patterns

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Frequency Count** | Counting occurrences | Anagrams, Top K |
| **Two Sum** | Find complements | Two Sum, Subarray Sum |
| **Index Mapping** | O(1) lookup by key | LRU, Random Pointers |
| **Set Operations** | Uniqueness/Intersection | Duplicates, Intersection |

## 📝 Complexity Guide

- **Average Case:** O(1) for lookup/insert/delete
- **Worst Case:** O(n) due to hash collisions
- **Space:** O(n) for n elements

## 🚀 Usage

```bash
# Clone the repository
git clone https://github.com/JanakPanchal/Hash-Map-Hash-Set-Interview-Questions.git

# Run any solution
python easy/two_sum.py

# Run tests
pytest tests/
