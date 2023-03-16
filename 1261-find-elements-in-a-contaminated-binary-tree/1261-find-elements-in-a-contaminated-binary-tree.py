# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = {0}
        root.val = 0
        level = [root]
        
        while level:
            next_level = []
            
            for child in level:
                if child.left:
                    child.left.val = 2*child.val + 1
                    next_level.append(child.left)
                    self.tree.add(child.left.val)
                    
                if child.right:
                    child.right.val = 2*child.val + 2
                    next_level.append(child.right)
                    self.tree.add(child.right.val)
                    
            level = next_level
        
        

    def find(self, target: int) -> bool:
        if target in self.tree:
            return True
        
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)