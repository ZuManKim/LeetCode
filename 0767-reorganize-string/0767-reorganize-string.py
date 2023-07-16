class Solution:
    def reorganizeString(self, s: str) -> str:
        
        char_counts = Counter(s)
        letter, max_cnt = char_counts.most_common(1)[0]
       
        if max_cnt > (len(s)+1)//2:
            return ""
        
        ans = [''] * len(s)
        idx = 0
        
        while char_counts[letter] != 0:
            ans[idx] = letter
            idx += 2
            char_counts[letter] -= 1
        
        for char, cnt in char_counts.items():
            while cnt > 0:
                if idx >= len(s):
                    idx = 1
                
                ans[idx] = char
                idx += 2
                cnt -= 1
                
        return "".join(ans)