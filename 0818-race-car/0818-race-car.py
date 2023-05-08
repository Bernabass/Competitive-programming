class Solution:
    def racecar(self, target: int) -> int:
        instruction = ("A", "R")
        level, seen = [(0, 1)], {(0, 1)}
        depth = 0
        
        while level:
            depth += 1
            next_level = []
            
            for position, speed in level:
                for command in instruction:
                    if (position + speed, 2*speed) not in seen and command == "A":
                        new_position = position + speed
                        new_speed = 2*speed
                        
                        if new_position == target:
                            return depth
                        
                        next_level.append((new_position, new_speed))
                        seen.add((new_position, new_speed))
                        
                    elif (position, -1*(speed//abs(speed))) not in seen and command == "R":
                        new_speed = -1*(speed//abs(speed))
                        
                        next_level.append((position, new_speed))
                        seen.add((position, new_speed))
                        
            level = next_level