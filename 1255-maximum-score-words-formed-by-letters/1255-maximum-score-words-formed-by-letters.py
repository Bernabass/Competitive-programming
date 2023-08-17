class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def CanBeFormed(word, collection):
            for char in word:
                if collection[char] <= 0:
                    return False
                collection[char] -= 1
                
            return True
        
        def total(word):
            total_score = 0
            
            for char in word:
                total_score += score[ord(char) - ord("a")]
                
            return total_score
        
        
        def dp(rem_letters, idx):
            if idx == len(words):
                return 0
            
            take = leave = 0
            curr_word = words[idx]
            if CanBeFormed(curr_word, deepcopy(rem_letters)):
                take = total(curr_word) + dp(rem_letters - Counter(curr_word), idx + 1)
                
            leave = dp(rem_letters, idx + 1)
            
            return max(take, leave)
        
        return dp(Counter(letters), 0)