"""
CSA06 - Design and Analysis of Algorithms | CO1 Assignment
Search strategies for locating a Registration Number in a student database.

Each algorithm has an *instrumented* version that returns (index_or_-1, comparisons)
so that the basic-operation count can be verified experimentally. Timing runs use
the same functions (counter overhead is identical in kind for all three, and the
raw operation counts are reported separately).

Approach 1 : Sequential (linear) search        - iterative, brute force, no preprocessing
Approach 2 : Binary search (recursive)         - decrease-and-conquer, needs sorted data
Approach 3 : Hash-table search (chaining)      - transform-and-conquer (space-time trade-off)
"""
import sys

sys.setrecursionlimit(10_000)

# ---------------------------------------------------------------- Approach 1
def linear_search(records, key):
    """Iterative brute-force scan. Returns (index, comparisons)."""
    comparisons = 0
    for i in range(len(records)):
        comparisons += 1                 # basic operation: records[i] == key
        if records[i] == key:
            return i, comparisons
    return -1, comparisons


# ---------------------------------------------------------------- Approach 2
def sort_records(records):
    """Preprocessing for binary search: O(n log n) comparison sort (Timsort)."""
    return sorted(records)


def binary_search_recursive(records, key, low=0, high=None, _count=None):
    """Recursive binary search on a SORTED list. Returns (index, comparisons)."""
    if _count is None:
        _count = [0]
    if high is None:
        high = len(records) - 1
    if low > high:                       # base case: empty sub-array
        return -1, _count[0]
    mid = (low + high) // 2
    _count[0] += 1                       # basic operation: key vs records[mid]
    if records[mid] == key:
        return mid, _count[0]
    if key < records[mid]:               # (second test treated as same 3-way compare)
        return binary_search_recursive(records, key, low, mid - 1, _count)
    return binary_search_recursive(records, key, mid + 1, high, _count)


def binary_search_iterative(records, key):
    """Iterative twin of Approach 2 (used only as a cross-check, not a 4th approach)."""
    low, high, comparisons = 0, len(records) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if records[mid] == key:
            return mid, comparisons
        if key < records[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, comparisons


# ---------------------------------------------------------------- Approach 3
class HashTable:
    """Separate-chaining hash table. Preprocessing = build_index(): O(n) expected."""
    A = 11400714819323198485             # Fibonacci hashing constant (2^64 / golden ratio)

    def __init__(self, n, load_factor=0.75):
        self.m = max(8, int(n / load_factor))
        self.buckets = [[] for _ in range(self.m)]
        self.size = 0

    def _h(self, key):
        return (((key * self.A) & 0xFFFFFFFFFFFFFFFF) * self.m) >> 64   # integer multiplicative hash

    def insert(self, key, value):
        self.buckets[self._h(key)].append((key, value))
        self.size += 1

    def search(self, key):
        """Returns (value_or_-1, comparisons)  -- comparisons = key compares in the chain."""
        comparisons = 0
        for k, v in self.buckets[self._h(key)]:
            comparisons += 1             # basic operation: stored key == key
            if k == key:
                return v, comparisons
        return -1, comparisons


def build_hash_index(records):
    """Preprocessing for Approach 3: insert every record, value = its position."""
    ht = HashTable(len(records))
    for pos, reg in enumerate(records):
        ht.insert(reg, pos)
    return ht
