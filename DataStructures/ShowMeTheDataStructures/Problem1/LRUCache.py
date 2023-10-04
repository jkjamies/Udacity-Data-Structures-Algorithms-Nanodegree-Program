"""
LRU Cache Implementation
"""

from collections import OrderedDict


class LRU_Cache(object):  # pylint: disable=C0103,R0205
    """
    LRU Cache Class
    """

    def __init__(self, capacity: int):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieve item from provided key. Return -1 if nonexistent.
        :param key:
        :return:
        """
        # Retrieve item from provided key. Return -1 if nonexistent.

        # If key doesn't exist, return -1
        if key not in self.cache:
            return -1
        # Move key to end of cache to show that it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: int, value: int) -> None:
        """
        Set the value if the key is not present in the cache. If the cache
        is at capacity remove the oldest item.
        :param key:
        :param value:
        """
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.

        # If cache capacity 0 or less, don't add any items
        if self.capacity <= 0:
            return

        # If cache capacity reached, remove the oldest item
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        # Insert key-value pair to cache and move to end
        self.cache[key] = value
        self.cache.move_to_end(key)


# Testing
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached its capacity
# and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null,
# empty or very large values

# Test Case 1
# None Value
our_cache.set(7, None)
print(our_cache.get(7))  # returns None

# Test Case 2
# Large Values
our_cache.set(8, 10 ** 20)
print(our_cache.get(8))  # returns 100000000000000000000

# Test Case 3
# Empty Cache
empty_cache = LRU_Cache(0)
empty_cache.set(1, 1)
print(empty_cache.get(1))  # returns -1 since capacity is 0
