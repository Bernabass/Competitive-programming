class Solution:
    def racecar(self, target: int) -> int:
        instruction = ("accelerate", "reverse")
        level, seen = [(0, 1)], {(0, 1)}
        depth = 0
        
        while level:
            depth += 1
            next_level = []
            
            for position, speed in level:
                for command in instruction:
                    if (position + speed, 2*speed) not in seen and command == "accelerate":
                        new_position = position + speed
                        new_speed = 2*speed
                        
                        if new_position == target:
                            return depth
                        
                        next_level.append((new_position, new_speed))
                        seen.add((new_position, new_speed))
                        
                    elif (position, -1*(speed//abs(speed))) not in seen and command == "reverse":
                        next_level.append((position, -1*(speed//abs(speed))))
                        seen.add((position, -1*(speed//abs(speed))))
                        
            level = next_level