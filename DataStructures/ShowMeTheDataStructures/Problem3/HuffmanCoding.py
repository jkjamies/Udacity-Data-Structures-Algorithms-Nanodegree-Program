# pylint: disable=C0103
"""
Huffman Coding Implementation
"""

import sys
import heapq
from collections import Counter


class Node:  # pylint: disable=R0903
    """
    Node class for Huffman Coding
    """

    def __init__(self, char, freq):
        """
        Constructor for Node class
        :param char:
        :param freq:
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """
        Less than comparison for Node class
        :param other:
        :return:
        """
        return self.freq < other.freq


def build_huffman_tree(data):
    """
    Build Huffman Tree
    :param data:
    :return:
    """
    frequency = Counter(data)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Loop until only one node is left in priority queue
    while len(priority_queue) > 1:
        # Pop two nodes with lowest frequency
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Create a new node with the sum of the frequencies
        merged = Node(None, left.freq + right.freq)
        # Set left and right nodes
        merged.left = left
        merged.right = right

        # Push new node to priority queue
        heapq.heappush(priority_queue, merged)

    # Return root node
    return priority_queue[0]


def build_codes(node, current_code, codez):
    """
    Build Huffman Codes
    :param node:
    :param current_code:
    :param codez:
    :return:
    """
    # If node is None, return
    if node is None:
        return

    # If node is a leaf, add to codes
    if node.char is not None:
        codez[node.char] = current_code
        return

    # Recursively build codes
    build_codes(node.left, current_code + "0", codez)
    build_codes(node.right, current_code + "1", codez)


def huffman_encoding(data):
    """
    Huffman Encoding
    :param data:
    :return:
    """
    # If data is empty, return empty string and None
    if not data:
        return "", None

    frequency = Counter(data)

    # If there's only one unique character
    if len(frequency) == 1:
        char, _ = frequency.most_common(1)[0]  # get the character
        return "0" * len(data), Node(char, len(data))

    root = build_huffman_tree(data)
    codez = {}

    # Build Huffman codes
    build_codes(root, "", codez)

    # Generate encoded data
    encode_data = "".join([codez[char] for char in data])

    # Return encoded data and root
    return encode_data, root


def huffman_decoding(data, tr):  # pylint: disable=C0103
    """
    Huffman Decoding
    :param data:
    :param tr:
    :return:
    """
    # If tree is None, return empty string
    if tr is None:
        return ""

    # If tree is a leaf, return char * len(data)
    if tr.char and not tr.left and not tr.right:
        return tr.char * len(data)

    decode_data = []
    current_node = tr

    # Loop through each bit in data
    for bit in data:
        # If bit is 0, go left - else go right
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        # If current node is a leaf, append char to decoded data
        if current_node.char:
            decode_data.append(current_node.char)
            current_node = tr

    # Return decoded data as a string
    return "".join(decode_data)


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"  # pylint: disable=C0103

    print("The size of the data is: {}\n".format(  # pylint: disable=C0209
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(  # pylint: disable=C0209
        a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(
        "The size of the encoded data is: {}\n"  # pylint: disable=C0209
        .format(sys.getsizeof(int(encoded_data, base=2)))
    )
    print(
        "The content of the encoded data is: {}\n"  # pylint: disable=C0209
        .format(encoded_data)
    )

    decoded_data = huffman_decoding(encoded_data, tree)

    print(
        "The size of the decoded data is: {}\n"  # pylint: disable=C0209
        .format(sys.getsizeof(decoded_data))
    )
    print(
        "The content of the encoded data is: {}\n"  # pylint: disable=C0209
        .format(decoded_data)
    )

# Test Cases

# Basic test
test_value = "test"  # pylint: disable=C0103
encoded_data, tree = huffman_encoding(test_value)
assert test_value == huffman_decoding(encoded_data, tree)
print("Test Case 1 Passed!: encoded and decoded data match \"test\"")

# Empty string
test_value = ""  # pylint: disable=C0103
encoded_data, tree = huffman_encoding(test_value)
assert test_value == huffman_decoding(encoded_data, tree)
print("Test Case 2 Passed!: encoded and decoded data match \"\"")

# Large repeated value
test_value = "a" * 10000  # pylint: disable=C0103
encoded_data, tree = huffman_encoding(test_value)
assert test_value == huffman_decoding(encoded_data, tree)
print("Test Case 2 Passed!: encoded and decoded data match \"a\" * 10000")
