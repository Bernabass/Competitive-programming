from BinaryTree import TreeNode
n1 = TreeNode(5)
n2 = TreeNode(7)
n3 = TreeNode(9)
n4 = TreeNode(13)
n5 = TreeNode(0)
n6 = TreeNode(15)
n7 = TreeNode(3)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.right = n6
n3.right = n7
def levelOrder(node):
    level = [node]
    res = [node.val]
    while level:
        levelX = []
        for i in level:
            if i.right:
                levelX.append(i.right)
                res.append(i.right.val)
            if i.left:
                levelX.append(i.left)
                res.append(i.left.val)
        level = levelX
    return res