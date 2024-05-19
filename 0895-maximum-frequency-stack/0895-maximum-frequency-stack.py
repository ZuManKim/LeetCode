class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.freq_stack = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq, freq_stack = self.freq, self.freq_stack
        freq[val] += 1
        freq_stack[freq[val]].append(val)
        self.max_freq = max(self.max_freq, freq[val])   

    def pop(self) -> int:
        freq, freq_stack, max_freq = self.freq, self.freq_stack, self.max_freq
        x = freq_stack[max_freq].pop()
        if not freq_stack[max_freq]:
            self.max_freq -= 1
        freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()