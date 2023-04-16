class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        for num in [tops[0], bottoms[0]]:
            
            if all(num in pair for pair in zip(tops, bottoms)):
                return len(tops) - max(tops.count(num), bottoms.count(num))
            
        return -1