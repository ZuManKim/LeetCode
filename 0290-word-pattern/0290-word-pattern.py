class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = {}
        words = s.split()
        
        if len(pattern) != len(words): return False
        if len(set(pattern)) != len(set(words)): return False
        
        for i in range(len(pattern)):
            if not word_dict.get(pattern[i]):
                word_dict[pattern[i]] = words[i]
            elif word_dict[pattern[i]] != words[i]:
                return False
        
        return True
                