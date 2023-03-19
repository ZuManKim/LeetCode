class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.freq_group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq, freq_group = self.freq, self.freq_group
        freq[val] += 1 
        self.max_freq = max(self.max_freq, freq[val])
        freq_group[freq[val]].append(val)

    def pop(self) -> int:
        freq, freq_group, max_freq  = self.freq, self.freq_group, self.max_freq
        res = freq_group[max_freq].pop()
        if not freq_group[max_freq]:
            self.max_freq -= 1
        freq[res] -= 1
        
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()