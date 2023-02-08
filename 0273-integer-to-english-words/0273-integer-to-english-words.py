class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        
        number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,1000,1000000,1000000000]
        number = list(map(str,number))
        words = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety Hundred Thousand Million Billion"
        convert = dict(zip(number,words.split()))
        
        num = str(num)
        num = [num[max(0,i-3):i] for i in range(len(num),0,-3)]
        num.reverse()
        n, toWord = len(num), []
        
        for chunk in num:
            if chunk not in convert:
                if len(chunk) == 2:
                    toWord.append(convert[str(int(chunk[0])*10)])
                    if int(chunk[1]):
                        toWord.append(convert[chunk[1]])
                    
                elif chunk:
                    if int(chunk[0]):
                        toWord.append(convert[chunk[0]])
                        toWord.append("Hundred")
                    if chunk[1] == "1":
                        toWord.append(convert[chunk[1:3]])
                    
                    else:   
                        if int(chunk[1]):
                            toWord.append(convert[str(int(chunk[1])*10)])

                        if int(chunk[2]):
                            toWord.append(convert[chunk[2]])
                       
            else:
                if len(chunk) > 2:
                    toWord.append("One")
                toWord.append(convert[chunk])
            
            if n > 1 and int(chunk):
                toWord.append(convert[str(10**(3*(n - 1)))])
            
            n -= 1
                                  
        return " ".join(toWord)