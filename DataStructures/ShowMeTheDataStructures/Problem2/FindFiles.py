"""
Find Files Implementation
"""

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # If suffix or path is None, return an empty list
    if suffix is None or path is None:
        return []

    # Structure to store all files found
    files_found = []

    # If path is a file and matches the suffix, return the path
    if os.path.isfile(path) and path.endswith(suffix):
        return [path]

    # If path is directory, loop through all items
    # and recursively search for files with the suffix
    if os.path.isdir(path):
        for item in os.listdir(path):
            # extend will add all items in the list to files_found
            # rather than append which will add the list itself
            files_found.extend(find_files(suffix, os.path.join(path, item)))

    return files_found


# Test Cases

# Test Case 1
# Find all ".c" files
print(find_files(".c", "./testdir"))

# Test Case 2
# Edge case - non-existing suffix
print(find_files(".invalid", "./testdir"))

# Test Case 3
# Edge case - empty directory path
print(find_files(".c", ""))

# Test Case 4
# Edge case - null suffix and path
print(find_files(None, None))

# Test Case 5
# Edge case - empty suffix
print(find_files("", "./testdir"))

# Test Case 6
# Find all ".h" files
print(find_files(".h", "./testdir"))
