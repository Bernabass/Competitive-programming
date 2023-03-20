class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        
        for i in range(len(flowerbed)-1):
            
            consc_sum = (flowerbed[i-1]+flowerbed[i]+flowerbed[i+1])     
            if not consc_sum:
                flowerbed[i] = 1
                n -= 1 
  
        return n <= 0