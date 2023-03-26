class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seq_set = set()
        for i in range(len(s)):
            if s[i:i+10] not in seq_set:
                seq_set.add(s[i:i+10])
            else: res.add(s[i:i+10])
        return list(res)