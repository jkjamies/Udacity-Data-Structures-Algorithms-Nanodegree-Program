# pylint: disable=C0103
"""
Union and Intersection Implementation
"""


class Node:  # pylint: disable=R0903
    """
    Node class for LinkedList
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    """
    LinkedList class
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        """
        Append a new element to the end of the list
        :param value:
        :return:
        """

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        """
        Return the size or length of the linked list
        :return:
        """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    """
    Return a new linked list that is the union of two linked lists
    :param llist_1:
    :param llist_2:
    :return:
    """
    set_1 = set()
    set_2 = set()

    node = llist_1.head
    # Add list_1 values to set_1
    while node:
        set_1.add(node.value)
        node = node.next

    node = llist_2.head
    # Add list_2 values to set_2
    while node:
        set_2.add(node.value)
        node = node.next

    # Union of set_1 and set_2
    union_set = set_1.union(set_2)

    # Create a new linked list with union_set values
    union_list = LinkedList()
    for value in union_set:
        union_list.append(value)

    return union_list


def intersection(llist_1, llist_2):
    """
    Return a new linked list that is the intersection of two linked lists
    :param llist_1:
    :param llist_2:
    :return:
    """
    set_1 = set()
    intersection_set = set()

    # Add list_1 values to set_1
    node = llist_1.head
    while node:
        set_1.add(node.value)
        node = node.next

    # Add list_2 values to intersection set if value is in set_1
    node = llist_2.head
    while node:
        if node.value in set_1:
            intersection_set.add(node.value)
        node = node.next

    # Create a new linked list with intersection values
    intersect_list = LinkedList()
    for value in intersection_set:
        intersect_list.append(value)

    return intersect_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases,
# such as null, empty or very large values

# Test Case 1
linked_list_test_1 = LinkedList()
linked_list_test_2 = LinkedList()
assert str(union(linked_list_test_1, linked_list_test_2)) == ""
assert str(intersection(linked_list_test_1, linked_list_test_2)) == ""
print("Test Case 1 Passed!: Union and intersection of empty lists are empty")

# Test Case 2
linked_list_test_1 = LinkedList()
linked_list_test_2 = LinkedList()
test_element = [1, 2, 3, 4, 5]
for i in test_element:
    linked_list_test_1.append(i)
assert str(
    union(
        linked_list_test_1, linked_list_test_2
    )
) == "1 -> 2 -> 3 -> 4 -> 5 -> "
assert str(
    intersection(
        linked_list_test_1, linked_list_test_2
    )
) == ""
print("Test Case 2 Passed!: Union not empty, intersection is empty")

# Test Case 3
linked_list_test_1 = LinkedList()
linked_list_test_2 = LinkedList()
test_element_1 = [1000000, 2000000, 3000000]
test_element_2 = [2000000, 4000000, 5000000]
for i in test_element_1:
    linked_list_test_1.append(i)
for i in test_element_2:
    linked_list_test_2.append(i)
assert str(
    union(
        linked_list_test_1, linked_list_test_2
    )
) == ("1000000 -> 2000000 -> 3000000 -> 4000000 -> 5000000 -> ")
assert str(
    intersection(
        linked_list_test_1, linked_list_test_2
    )
) == "2000000 -> "
print("Test Case 3 Passed!: Union and intersection are not empty")
