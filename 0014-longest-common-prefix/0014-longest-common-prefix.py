class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for i in range(1,len(strs)):
            count = 0
            temp = ""
            while count < min(len(strs[i]),len(common)):
                if common[count] == strs[i][count]:
                    temp += common[count]
                    count += 1
                else:
                    break
            common = temp
        return common