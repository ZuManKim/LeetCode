class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A = B = 0
        
        for i in range(len(colors)-2):
            if colors[i]==colors[i+1]==colors[i+2]:
                if colors[i] == 'A':
                    A += 1
                else:
                    B += 1
        
        return A > B        