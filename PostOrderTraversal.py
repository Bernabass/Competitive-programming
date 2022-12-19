from BinaryTree import TreeNode
from LevelOrderTraversal import levelOrder
n1 = TreeNode(-10)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
# n6 = TreeNode(15)
# n7 = TreeNode(3)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
# n4.right = n6
# n3.right = n7
def postOrder(node):
    res = levelOrder(node)
    res.reverse()
    return res
print(postOrder(n1))
