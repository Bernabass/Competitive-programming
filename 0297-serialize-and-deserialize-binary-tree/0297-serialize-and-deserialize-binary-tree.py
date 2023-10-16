# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        ans = []
        
        def dfs(node):
            if not node:
                ans.append("#")
                return
            
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return "eh".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """        
        idx = 0
        data = data.split("eh")
        def dfs():
            nonlocal idx
            if data[idx] == "#":
                return None
            
            node = TreeNode(int(data[idx]))
            idx += 1
            node.left = dfs()
            idx += 1
            node.right = dfs()
            
            return node
        
        return dfs()
        
        
            
            


    # Your Codec object will be instantiated and called as such:
    # ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))