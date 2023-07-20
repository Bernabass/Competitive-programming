class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for val in asteroids:
            flag = True
            while flag and stack and stack[-1] > 0 and val < 0:
                prev, curr = abs(stack[-1]), abs(val)
                if prev == curr:
                    stack.pop()
                    flag = False
                    
                elif prev < curr:
                    stack.pop()
                    
                else:
                    flag = False
              
            if flag:
                stack.append(val)
                    
        return stack