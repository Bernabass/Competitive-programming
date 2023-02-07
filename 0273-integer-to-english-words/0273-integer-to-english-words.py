class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        num = str(num)
        digit = len(num)
        number = [num[max(0,i-3):i] for i in range(len(num),0,-3)]
        number.reverse()
        nums = list(range(1,20))
        nums.extend(range(20,100,10))
        nums.extend([100, 1000,1000000,1000000000])
        toWord = []
        
        words = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety Hundred Thousand Million Billion"
        
        info = dict(zip(nums,words.split()))
        n = len(number)

        for idx, chunk in enumerate(number):
            if int(chunk) not in info:
                if len(chunk) == 2:
                    flag = True
                    toWord.append(info[int(chunk[0])*10])
                    if toWord.append(info[int(chunk[1])]):
                        toWord.append(info[int(chunk[1])])
                    
                elif int(chunk) != 0:
            
                    if int(chunk[0]) != 0:
                        toWord.append(info[int(chunk[0])])
                        toWord.append("Hundred")
                    if int(chunk[1]) == 1:
                        toWord.append(info[int(chunk[1:3])])
                    
                    else:   
                        if int(chunk[1]) != 0:
                            toWord.append(info[int(chunk[1])*10])

                        if int(chunk[2])!= 0:
                            toWord.append(info[int(chunk[2])])
                   
                    
            else:
                if len(str(int(chunk))) > 2:
                    toWord.append("One")
                toWord.append(info[int(chunk)])
            
            if n > 1 and int(chunk):
                toWord.append(info[10**(3*(n - 1))])
            
            n -= 1
                                  
        return " ".join(toWord)