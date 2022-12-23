class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1) , len(word2)
        pointer = 0
        res = ""
        word1 = list(word1)
        word2 = list(word2)
        if n1 > n2:
            temp = (n1 - n2)*['']
            word2.extend(temp)
        else:
            temp = (n2 - n1)*['']
            word1.extend(temp)
        while pointer < len(word1):
            res += word1[pointer] + word2[pointer]
            pointer += 1
        return res