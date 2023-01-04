class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string = str(num)
        substring, n = deque(), len(string)
        k_beauty = left = right = 0
        
        for idx in range(k):
            substring.append(string[idx])
            right += 1
        
        cur_num = int("".join(substring))
        if cur_num and num % cur_num  == 0:
            k_beauty += 1
        
        while right < n:
            substring.popleft()
            substring.append(string[right])
            cur_num = int("".join(substring))
            if cur_num and num % cur_num  == 0:
                k_beauty += 1
            right += 1
            left += 1
            
        return k_beauty