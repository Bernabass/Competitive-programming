class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        freq=Counter(changed)
        original=[]
        modified=[]
        for i in changed:
            doubled=i*2
            if freq[i]>0 and doubled in freq and freq[doubled]>0:
                original.append(i)
                modified.extend([i,doubled])
                freq[doubled]-=1
                freq[i]-=1
        else:
            modified.sort()
            if modified==changed:
                return original
            else:
                return []