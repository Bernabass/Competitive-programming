class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m , n = len(mat) , len(mat[0])
        direc = True
        cell , stack , res = [0,0] , [] , []
        def traverse(cell,direc):
            i , j = cell[0] , cell[1]
            while 0 <= i < m and 0 <= j < n:
                stack.append([i,j])
                res.append(mat[i][j])
                if direc:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1   
            direc = not direc
    
        while cell != [m-1,n-1] :
            if direc:
                traverse(cell,True)
                if stack[-1][1] + 1 < n:
                    i , j = stack[-1][0] , stack[-1][1] + 1
                else:
                    i , j = stack[-1][0] + 1 , stack[-1][1]
                cell = [i,j]
                direc = False
                continue
            else:
                
                traverse(cell,False)
                if stack[-1][0] + 1 < m:
                    i , j = stack[-1][0] + 1 , stack[-1][1]
                else:
                    i , j = stack[-1][0] , stack[-1][1] + 1
                cell = [i,j]
                direc = True
        res.append(mat[m-1][n-1])
        return res