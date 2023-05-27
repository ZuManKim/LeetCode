class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num
        
        while sqrt**2 > num:
            sqrt = (sqrt + num/sqrt) // 2
        
        return sqrt**2 == num