class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node()
        node.value = value

        if self.root is None:
            self.root = node
            return True

        curr_root = self.root
        while True:
            if curr_root.value == value:
                return False
            if value < curr_root.value:
                if curr_root.left is None:
                    curr_root.left = node
                    return True
                curr_root = curr_root.left
            if value > curr_root.value:
                if curr_root.right is None:
                    curr_root.right = node
                    return True
                curr_root = curr_root.right

    def contains(self, value):
        if self.root is None:
            return False

        curr_root = self.root
        while curr_root is not None:
            if value < curr_root.value:
                curr_root = curr_root.left
            elif curr_root.value < value:
                curr_root = curr_root.right
            else:
                return True
        return False


bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)

print(bst.contains(1))
print(bst.contains(5))
