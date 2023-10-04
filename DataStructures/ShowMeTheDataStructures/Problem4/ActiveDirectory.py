# pylint: disable=C0103
"""
Active Directory Implementation
"""


class Group(object):  # pylint: disable=R0205
    """
    Provided Group class
    """

    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        """
        Add group to groups list
        :param group:
        :return:
        """
        self.groups.append(group)

    def add_user(self, user):
        """
        Add user to users list
        :param user:
        :return:
        """
        self.users.append(user)

    def get_groups(self):
        """
        Get groups list
        :return:
        """
        return self.groups

    def get_users(self):
        """
        Get users list
        :return:
        """
        return self.users

    def get_name(self):
        """
        Get group name
        :return:
        """
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"  # pylint: disable=C0103
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # If user is in group, return True
    if user in group.get_users():
        return True

    # Loop through each sub-group and recursively check if user is in group
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True

    # If user is not in group, return False
    return False


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null,
# empty or very large values

# Test Case 1
USER_TO_CHECK = "sub_child_user"
group_to_check = parent
assert is_user_in_group(USER_TO_CHECK, group_to_check) is True
print("Test Case 1 Passed!: sub_child_user is in parent group")

# Test Case 2
USER_TO_CHECK = "non_existent_user"
group_to_check = parent
assert is_user_in_group(USER_TO_CHECK, group_to_check) is False
print("Test Case 2 Passed!: non_existent_user is not in parent group")

# Test Case 3
USER_TO_CHECK = None
group_to_check = parent
assert is_user_in_group(USER_TO_CHECK, group_to_check) is False
print("Test Case 3 Passed!: None is not in parent group")
