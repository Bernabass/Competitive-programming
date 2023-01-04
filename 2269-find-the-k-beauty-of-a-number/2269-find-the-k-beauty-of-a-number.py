class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        '''
        The problem is solved using 
        the fixed sliding window approach.
        And to reduce time complexity "deque" is
        used instead of string concatination or list.
        '''
        string = str(num)
        substring, n = deque(), len(string)
        k_beauty = left = right = 0
        
        # Preparing the fixed window.
        for idx in range(k):
            substring.append(string[idx])
            right += 1
    
        # Checking if there is a k-beauty in the prepared window.
        cur_num = int("".join(substring))
        if cur_num and num % cur_num  == 0:
            k_beauty += 1
        
        # Counting the number of k-beauty by sliding the window
        while right < n:
            substring.popleft()
            substring.append(string[right])
            cur_num = int("".join(substring))
            if cur_num and num % cur_num  == 0:
                k_beauty += 1
            right += 1
            left += 1
            
        return k_beauty