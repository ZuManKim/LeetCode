import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        list_string = list(map(str, nums))
        list_string.sort(key=functools.cmp_to_key(lambda x, y: self.cmp(y+x, x+y)))
        res = ''.join(list_string)
        return '0' if res[0] == '0' else res
    
    def cmp(self, x, y): 
        return (x > y) - (x < y)