class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_dict = Counter(text)
        min_cnt = min(count_dict['b'], count_dict['a'], count_dict['l']//2, 
                      count_dict['o']//2, count_dict['n'])
        
        return min_cnt