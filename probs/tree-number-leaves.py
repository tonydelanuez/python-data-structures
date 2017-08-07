class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def number_of_leaves(self,root):
        if root == None:
            return 0
        if root.left_child == None and root.right_child == None:
            return 1
        return self.number_of_leaves(root.left_child) + self.number_of_leaves(root.right_child)