class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        freq, ans = defaultdict(int), []
        heap = []
        
        for char in s:
            if char.lower() in vowels:
                freq[char] += 1
                
        for char, count in freq.items():
            heappush(heap, (char, count))

        for char in s:
            if char.lower() in vowels:
                min_char, count = heappop(heap)
                ans.append(min_char)
                count -= 1
                if count:
                    heappush(heap, (min_char, count))
                    
            else:
                ans.append(char)
                     
        return "".join(ans)