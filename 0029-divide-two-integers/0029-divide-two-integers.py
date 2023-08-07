class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
                        
        sign = "-"
        if divisor > 0 <= dividend or (divisor < 0 > dividend):
            sign = ""
            
        def do(x):
            ans = int(sign + str(x))
            if ans < 0:
                ans = max(-2**31, ans)

            else:
                ans = min(2**31 - 1, ans)
                
            return ans
            
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            return do(dividend)
        
        def calc(num):
            ans = rem = idx = 0
            while rem + num:
                curr = rem
                if num & 1:
                    curr += divisor
        
                ans |= (curr & 1) << idx
                
                if curr & 1:
                    rem = (curr - 1) >> 1
                    
                else:
                    rem = curr >> 1
                    
                num >>= 1
                idx += 1
                
            return ans
            
        left = 0
        right = dividend
        
        while left <= right:
            range_sum = left + right
            
            if 1 & range_sum:
                mid = (range_sum + 1) >> 1
                
            else:
                mid = range_sum >> 1
                
            curr = calc(mid)
                
            if curr == dividend:
                return do(mid)
            
            elif curr < dividend:
                if calc(mid + 1) > dividend:
                    return do(mid)
                
                left = mid + 1
                      
            else:
                right = mid - 1
