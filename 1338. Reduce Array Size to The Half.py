class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length=(len(arr)+1)//2
        count=[1]
        output=[]
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i]:
                count[-1]+=1
            else:
                count.append(1)
        count.sort(reverse=True)
        for j in count:
            if j-length>=0:
                output.append(j)
                return (len(output))
            else:
                length=length-j
                output.append(j)
        else:
            return (len(output))