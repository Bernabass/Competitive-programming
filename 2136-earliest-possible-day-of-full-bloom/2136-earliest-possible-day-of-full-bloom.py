class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(growTime)
        temp = []
        for i in range(n):
            temp.append([growTime[i],plantTime[i]])
        temp.sort(reverse = True)

        for idx, val in enumerate(temp):
            plantTime[idx] = val[1]
            growTime[idx] = val[0]
         
        Pday = -1
        earliest = 0
        for i in range(n):
            Pday += plantTime[i]
            Gday = Pday + growTime[i]
            Bday = Gday + 1
            earliest = max(earliest, Bday)
            
            
        return earliest