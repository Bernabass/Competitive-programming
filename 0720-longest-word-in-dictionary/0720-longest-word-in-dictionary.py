class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        prev = set()
        longest_word = ""
        
        for i in range(len(words)):
            word = words[i]
            curr = ""
            
            for j in range(len(word) - 1):
                char = word[j]
                curr += char
                if curr not in prev:
                    break
                    
            else:
                if len(word) > len(longest_word):
                    longest_word = word
                    
                elif len(word) == len(longest_word):
                    longest_word = min(longest_word, word)
                    
            prev.add(word)
                    
        return longest_word