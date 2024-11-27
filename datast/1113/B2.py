class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def delete_node(root, value):
    if root is None:
        return root

    if value < root.val:
        root.left = delete_node(root.left, value)
    elif value > root.val:
        root.right = delete_node(root.right, value)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = find_min(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.val)

    return root


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def print_tree(root, level=0, prefix="Root: "):
    """Prints the tree in a readable format."""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


# Example Usage
if __name__ == "__main__":
    # Create a sample tree
    root = TreeNode(50)
    root.left = TreeNode(30)
    root.right = TreeNode(70)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(40)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)

    print("Initial Tree:")
    print_tree(root)

    print("\nDeleting node 70:")
    root = delete_node(root, 70)
    print_tree(root)

    print("\nDeleting node 50:")
    root = delete_node(root, 50)
    print_tree(root)
