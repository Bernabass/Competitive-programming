class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = defaultdict(list)
        count = 0
        
        for idx, char in enumerate(s):
            indices[char].append(idx)
                        
        for word in words:
            prev = 0
            for i in range(len(word)):
                arr = indices[word[i]]
                idx = bisect_left(arr, prev)
                
                if idx >= len(arr) or arr[idx] < prev:
                    break
                    
                prev = arr[idx] + 1
            else:
                count += 1
                
        return count