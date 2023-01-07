class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        sequence = s[:10]
        repeated = {sequence:1}
        for idx in range(10,n):
            sequence = list(sequence)
            sequence.pop(0)
            sequence.append(s[idx])
            sequence = "".join(sequence)
            if sequence in repeated:
                if repeated[sequence] > 0:
                    ans.append(sequence)
                    repeated[sequence] -= 1
            else:
                repeated[sequence] = 1
        
        return ans