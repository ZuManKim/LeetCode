class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        total = 2 ** k
        all_ones = total - 1
        hash_val = 0
        check = set()
        
        for i in range(len(s)):
            hash_val = ((hash_val << 1) & all_ones) | (int(s[i]))
            
            if i >= k-1:
                check.add(hash_val)
                if len(check) == total: 
                    return True
        
        return False