class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        check=list(zip(l,r))
        output=[]
        for i in range(len(check)):
            sub=nums[check[i][0]:check[i][1]+1]
            sub.sort()
            d=sub[1]-sub[0]
            for j in range(2,len(sub)):
                if sub[j]-sub[j-1]!=d:
                    output.append(False)
                    break
            else:
                output.append(True)
        return output