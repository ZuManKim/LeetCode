class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = collections.Counter(chars)
        
        ans = 0
        for word in words:
            word_count = collections.Counter(word)
            
            if all(word_count[char] <= counts[char] for char in word_count):
                ans += len(word)        
        
        return ans