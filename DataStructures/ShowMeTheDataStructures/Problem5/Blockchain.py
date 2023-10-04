# pylint: disable=C0103
"""
Blockchain Implementation
"""

import hashlib
import time


class Block:  # pylint: disable=R0903
    """
    Block class for Blockchain
    """

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        """
        Calculate hash for block
        :return:
        """
        sha = hashlib.sha256()
        hash_str = (
            "{}{}{}".format(  # pylint: disable=C0209
                self.data,
                self.timestamp,
                self.previous_hash
            ).encode('utf-8')
        )
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:  # pylint: disable=R0903
    """
    Blockchain class
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a block to the end of the chain
        :param data:
        :return:
        """
        if not data:
            return

        timestamp = time.gmtime()  # Using Greenwich Mean Time
        if not self.head:
            previous_hash = None
            self.head = Block(timestamp, data, previous_hash)
        else:
            curr_block = self.head
            while curr_block.next:
                curr_block = curr_block.next
            previous_hash = curr_block.hash
            curr_block.next = Block(timestamp, data, previous_hash)


# Add your own test cases: include at least three test cases
# and two of them must include edge cases,
# such as null, empty or very large values

# Test Case 1
bc = Blockchain()
bc.append("Block 1 Data")
bc.append("Block 2 Data")
assert bc.head.data == "Block 1 Data"
assert bc.head.next.data == "Block 2 Data"
assert bc.head.hash != bc.head.next.hash
print("Test Case 1 Passed!: Blockchain has 2 blocks with correct data")

# Test Case 2
bc = Blockchain()
bc.append("")
assert bc.head is None
print("Test Case 2 Passed!: Blockchain has no blocks")

# Test Case 3
bc = Blockchain()
lot_of_js = "J" * (10 ** 6)
bc.append(lot_of_js)
assert bc.head.data == lot_of_js
assert bc.head.hash is not None
print("Test Case 3 Passed!: Blockchain has 1 block with a lot of data")

# Test Case 4
bc = Blockchain()
num_blocks = 10 ** 4
for i in range(num_blocks):
    bc.append(f"Block {i}")
current_block = bc.head
count = 0
while current_block:
    count += 1
    current_block = current_block.next
assert count == num_blocks
print("Test Case 4 Passed!: Blockchain has 10000 blocks")
