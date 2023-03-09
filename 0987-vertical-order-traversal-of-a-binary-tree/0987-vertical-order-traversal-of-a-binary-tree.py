# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def sort_nodes(col, new_node):
            res = [new_node]
            while col and new_node[1] == col[-1][1]:
                res.append(col.pop())
                
            res.sort()
            col.extend(res)
            
            return col
        
        result = []
        columns = defaultdict(list)
        curr_level = [[root,(0,0)]]
        columns[0].append([root.val, 0])
        
        while curr_level:
            next_level = []
            
            for child, location in curr_level:
                if child.left:
                    row, col = location[0] + 1, location[1] - 1
                    next_level.append([child.left,(row, col)])
                    columns[col] = sort_nodes(columns[col], [child.left.val, row])
                    
                if child.right:
                    row, col = location[0] + 1, location[1] + 1
                    next_level.append([child.right,(row, col)])
                    columns[col] = sort_nodes(columns[col], [child.right.val, row])
                    
            curr_level = next_level
        
        sorted_columns = dict(sorted((columns).items()))
        for val in sorted_columns.values():
            nodes = []
            for node, row in val:
                nodes.append(node)
                
            result.append(nodes)
                
        return result