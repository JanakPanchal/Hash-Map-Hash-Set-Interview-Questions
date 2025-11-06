# Hash Map Complexity Cheatsheet

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search | O(1) | O(n) |
| Access by key | O(1) | O(n) |

## Space Complexity

- **Hash Map/Set:** O(n) where n = number of elements

## Collision Handling

- **Chaining:** Each bucket contains a linked list
- **Open Addressing:** Find next available slot

## Load Factor

- **Optimal:** 0.7 - 0.75
- **Resize:** When load factor exceeded, double size and rehash

## Python Specifics

| Data Structure | Ordered | Immutable Keys | Use Case |
|----------------|---------|----------------|----------|
| `dict` | 3.7+ | Yes | General purpose |
| `set` | No | Yes | Membership testing |
| `defaultdict` | No | Yes | Auto-initialization |

## When to Use

1. **Frequency Counting:** Count occurrences
2. **Two Sum:** Find complements
3. **Index Mapping:** Store positions
4. **Set Operations:** Unions, intersections
5. **Caching/Memoization:** Store computed results