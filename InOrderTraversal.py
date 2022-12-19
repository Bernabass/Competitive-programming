from BinaryTree import TreeNode
n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(2)
# n4 = TreeNode(13)
# n5 = TreeNode(0)
# n6 = TreeNode(15)
# n7 = TreeNode(3)
n1.left = n2
# n1.right = n3
# n2.left = n4
n2.right = n3
# n4.right = n6
# n3.right = n7
def iterative_inorder(node):
    stack = [ ]
    current = n1
    res = [ ]
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            res.append(current.val)
            current = current.right
    return res
res2 = [ ]
def recursive_inorder(node):
    if not node:
        return
    recursive_inorder(node.left)
    res2.append(node.val)
    recursive_inorder(node.right)
    return res2
print(recursive_inorder(n1))
print(iterative_inorder(n1))