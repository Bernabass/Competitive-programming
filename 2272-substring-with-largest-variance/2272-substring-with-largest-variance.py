class Solution:
    def largestVariance(self, s: str) -> int:
        uniques = list(set(s))
        max_var, n = 0, len(uniques)
        
        def pair_sum(char1, char2, sign):
            info = defaultdict(int)
            info[char1], info[char2] = sign, -sign
            
            if sign > 0:
                pos_ones = s.count(char1)
                neg_ones = s.count(char2)
                
            else:
                pos_ones = s.count(char2)
                neg_ones = s.count(char1)
                
            has_pos_ones = has_neg_ones = False
            max_sum = curr_sum = 0

            for char in s:
                val = info[char]
                
                if curr_sum < 0 and pos_ones and neg_ones:
                    curr_sum = 0
                    has_ones = has_neg_ones = False
                    
                if val == 1:
                    curr_sum += 1
                    has_pos_ones = True
                    pos_ones -= 1
                    
                elif val == -1:
                    curr_sum -= 1
                    has_neg_ones = True
                    neg_ones -= 1
                    
                if has_pos_ones and has_neg_ones:
                    max_sum = max(max_sum, curr_sum)
                
            return max_sum

        for i in range(n):
            for j in range(i+1, n):
                char1, char2 = uniques[i], uniques[j]
                curr_var1 = pair_sum(char1, char2, 1)
                curr_var2 = pair_sum(char1, char2, -1)
                max_var = max([max_var, curr_var1, curr_var2])
                
        return max_var