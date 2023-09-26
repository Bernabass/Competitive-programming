class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        indices = defaultdict(list)
        ans = ""
        
        for idx, char in enumerate(s):
            indices[char].append(idx)
                        
        for word in dictionary:
            prev = 0
            for i in range(len(word)):
                arr = indices[word[i]]
                idx = bisect_left(arr, prev)
                
                if idx >= len(arr) or arr[idx] < prev:
                    break
                    
                prev = arr[idx] + 1
            else:
                if len(word) > len(ans):
                    ans = word
                    
                elif len(word) == len(ans):
                    ans = min(ans, word)
                
        return ans