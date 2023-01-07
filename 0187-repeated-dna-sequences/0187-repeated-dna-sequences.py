class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        ans = set()
        repeated = {s[:10]}
        for idx in range(1,n - 9):
            sequence = s[idx:idx+10]
            if sequence in repeated:
                ans.add(sequence)
            repeated.add(sequence)
        
        return [*(ans)]