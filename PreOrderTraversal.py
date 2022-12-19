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
def iterative_Preorder(node):
    stack = [ ]
    current = n1
    res = [ ]
    while current or stack:
        if current:
            stack.append(current)
            res.append(current.val)
            current = current.left
        else:
            current = stack.pop()
            current = current.right
    return res
res2 = [ ]
def recursive_Preorder(node):
    if not node:
        return
    res2.append(node.val)
    recursive_Preorder(node.left)
    recursive_Preorder(node.right)
    return res2
