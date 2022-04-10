#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        m=arr[i]
        for j in range(i,len(arr)):
            if arr[j]<=m:
                m=arr[j]
                idx=j
        return idx
        
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            idx=self.select(arr, i)
            m=arr[idx]
            arr[idx]=arr[i]
            arr[i]=m
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends