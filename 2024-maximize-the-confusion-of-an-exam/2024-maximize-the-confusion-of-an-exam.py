class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = max_consecutive = 0
        true = false = 0
        
        for right in range(n):
            if answerKey[right] == "T":
                true += 1
                
            else:
                false += 1
                
            while min(true,false) > k:
                if answerKey[left] == "T":
                    true -= 1

                else:
                    false -= 1
                    
                left += 1
                
            max_consecutive = max(max_consecutive, right - left + 1)
            
            
        return max_consecutive
        