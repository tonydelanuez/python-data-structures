'''
Input:

      7
    /   \
   3     9
  / \   / \
 2   4 8  10


Output:

7
3 9
2 4 8 10
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    levels = []
    traverseDown(root, levels, 0)
    return levels


"""
After 7:
[[7]]

list()
set()

3 sees:
[[7]]

9 sees:
[[7]]

[[7], [3]]
[[7], [9]]
"""

def traverseDown(root, levels, depth):
    if not root:
        return

    #adding a list for that level
    if (len(levels) == depth):
        levels.append([])

    levels[depth].append(root.data)

    traverseDown(root.left, levels, depth + 1)
    traverseDown(root.right, levels, depth + 1)



root = Node(7)
root.left = Node(3)
root.right = Node(9)
l1 = root.left
l2 = root.right
l1.left = Node(2)
l1.right = Node(4)
l2.left = Node(8)
l2.right = Node(10)



print(levelOrder(root))
