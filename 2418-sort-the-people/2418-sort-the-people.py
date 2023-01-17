class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        temp = [heights[0]]
        
        def insert_sort(arr):
            m = len(arr)
            for i in range(m-1,0,-1):
                if arr[i] > arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    names[i], names[i-1] = names[i-1], names[i]
                    
        for i in range(1,n):
            temp.append(heights[i])
            insert_sort(temp)
            
        return names