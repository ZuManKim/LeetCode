class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A = B = 0
        
        for i in range(len(colors)-2):
            if colors[i:i+3] == 'AAA':
                A += 1
            elif colors[i:i+3] == 'BBB':
                B += 1
        
        return A > B        