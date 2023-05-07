class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        level, seen = [(0, 1)], {(0, 1)}
        depth = 0

        while level:
            depth += 1
            next_level = []
            
            for copy, paste in level:
                if (copy+paste, copy) not in seen and paste+copy <= 1000:
                    if copy+paste == n:
                        return depth
                    
                    next_level.append((copy, copy+paste))
                    seen.add((copy, copy+paste))
                    
                if (paste, paste) not in seen and paste <= 1000:
                    next_level.append((paste, paste))
                    seen.add((paste, paste))
                    
            level = next_level