class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def valid(word, freq):
            used = defaultdict(int)
            for char in word:
                if freq[char] - used[char] <= 0:
                    return False
                
                used[char] += 1
            
            return True
        
        def TotalScore(word):
            return sum(score[ord(char) - ord("a")] for char in word)
        
        def back_track(idx, freq):
            if idx == len(words):
                return 0
            
            take = leave = 0
            curr_word = words[idx]
            if valid(curr_word, freq):
                take = TotalScore(curr_word) + back_track(idx + 1, freq - Counter(curr_word))
                
            leave = back_track(idx + 1, freq)
            
            return max(take, leave)
        
        return back_track(0, Counter(letters))