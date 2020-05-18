class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        "two pointers approach and "
        "sorting "
        people.sort(reverse = True)
        left = boats = 0
        right = len(people)-1
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1   
            else:
                left += 1
                
            boats += 1 
        return boats