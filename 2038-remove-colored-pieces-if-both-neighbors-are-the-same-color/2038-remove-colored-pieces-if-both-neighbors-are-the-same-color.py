class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        kitya = "A" if colors[-1] == "B" else "B"
        colors = list(colors) + [kitya]
        alice = bob = 0
        consec_A = consec_B = 0
        
        for char in colors:
            if char == "A":
                consec_A += 1
                if consec_B > 2:
                    bob += consec_B - 2
                consec_B = 0
                
            else:
                consec_B += 1
                if consec_A > 2:
                    alice += consec_A - 2
                consec_A = 0
       
        return alice > bob