class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def make_child(val):
            if val:
                return [1,0]
            
            return [0,1]
        
        
        command = deque()
        while k > 1:
            if k % 2:
                command.appendleft("L")
            else:
                command.appendleft("R")
                
            k = math.ceil(k/2)
           
        curr = 0
        for cmd in command:
            child = make_child(curr)
            
            if cmd == "L":
                curr = child[0]
                
            else:
                curr = child[1]
                
        
        return curr
            