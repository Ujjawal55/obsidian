class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height is set to 1 for a new node


class AVLTree:
    # Utility function to get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Utility function to get the balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotation (single right rotation)
    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # New root after rotation

    # Left rotation (single left rotation)
    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # New root after rotation

    # Insert a key into the AVL tree and balance the tree
    def insert(self, root, key):
        # 1. Perform normal BST insertion
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor to check whether this node became unbalanced
        balance = self.get_balance(root)

        # 4. Apply rotations based on the balance factor

        # Left-Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right-Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Utility function to print in-order traversal of the tree
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.key, end=" ")
            self.in_order_traversal(root.right)


# Example usage:
avl_tree = AVLTree()
root = None

# Inserting nodes
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl_tree.insert(root, key)

# Print the in-order traversal of the balanced AVL tree
print("In-order traversal of the AVL tree is:")
avl_tree.in_order_traversal(root)
print()
