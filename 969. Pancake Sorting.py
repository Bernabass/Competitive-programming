class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        length=len(arr)-1
        out=[]
        for i in range(length,-1,-1):
            mod=arr[:]
            if arr[i]==i+1:
                continue
            else:
                max=i+1
                idx=arr.index(max)
                out.append(idx+1)
                arr=arr[:idx+1]
                arr.reverse()
                cut=mod[idx+1:]
                arr.extend(cut)
                new=arr[:]
                arr=arr[:max]
                out.append(max)
                arr.reverse()
                cut=new[max:]
                arr.extend(cut)
        for j in out:
            if j==1:
                out.remove(j)
        return out