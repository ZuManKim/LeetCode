class MinStack:

    def __init__(self):
        self.q = []

    def push(self, val: int) -> None:
        cur_min = self.getMin()
        if cur_min is None or val < cur_min:
            cur_min = val
        self.q.append((val, cur_min))
        
    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        return self.q[-1][0] if self.q else None

    def getMin(self) -> int:
        return self.q[-1][-1] if self.q else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()