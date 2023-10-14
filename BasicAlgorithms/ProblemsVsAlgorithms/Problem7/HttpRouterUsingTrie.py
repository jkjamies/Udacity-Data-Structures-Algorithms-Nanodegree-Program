# pylint: disable=C0103
"""
Http Router using a Trie
"""


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    """
    A RouteTrie will store our routes and their associated handlers
    """

    def __init__(self):
        """
        Initialize the trie with an root node and a handler,
        """
        # Initialize the trie with an root node and a handler,
        # this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path_parts, handler):
        """
        Similar to our previous example you will want to recursively add nodes
        :param path_parts:
        :param handler:
        :return:
        """
        # Similar to our previous example you will want to
        # recursively add nodes. Make sure you assign the handler
        # to only the leaf (deepest) node of this path
        current_node = self.root
        # Iterate through the path parts
        for part in path_parts:
            # If part not in current node's children, add it
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            # Move to the next node
            current_node = current_node.children[part]
        # Assign the handler to the leaf node
        current_node.handler = handler

    def find(self, path_parts):
        """
        Starting at the root, navigate the Trie to find a match for this path
        :param path_parts:
        :return:
        """
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        # Iterate through the path parts
        for part in path_parts:
            # If part in current node's children, move to the next node
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                # If part not in current node's children, return None
                return None
        # Return the handler for a match
        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode...
# with one additional element, a handler.
class RouteTrieNode:  # pylint: disable=R0903
    """
    A RouteTrieNode will be similar to our autocomplete TrieNode...
    """

    def __init__(self):
        """
        Initialize the node with children as before, plus a handler
        """
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, part):
        """
        Insert the node as before
        :param part:
        :return:
        """
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    """
    The Router class will wrap the Trie and handle
    """

    def __init__(self, root_handler, not_found_handler):
        """
        Create a new RouteTrie for holding our routes
        :param root_handler:
        :param not_found_handler:
        """
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not
        # found responses as well!
        self.route_trie = RouteTrie()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        """
        Add a handler for a path
        :param path:
        :param handler:
        :return:
        """
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        """
        lookup path (by parts) and return the associated handler
        :param path:
        :return:
        """
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # If path is "/", return root handler
        if path == "/":
            return self.root_handler

        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)

        # If handler found, return it
        if handler:
            return handler

        # If handler not found, return not found handler
        return self.not_found_handler

    def split_path(self, path):
        """
        You need to split the path into parts for
        :param path:
        :return:
        """
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        # If path is "/", return empty list
        if path == "/":
            return []
        # Return path parts with stripped leading and split trailing slashes
        return path.strip("/").split("/")


# Here are some test cases and expected outputs
# you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

# some lookups with the expected output

# should print 'root handler'
print(router.lookup("/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
# should print 'about handler'
print(router.lookup("/home/about"))
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
