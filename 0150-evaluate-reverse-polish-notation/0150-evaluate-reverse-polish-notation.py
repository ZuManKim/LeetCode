class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                tmp = self.operate(a, b, token)
                stack.append(tmp)
            else:
                stack.append(int(token))
        
        return stack.pop()
    
    def operate(self, a, b, token):
        if token == "+":
            return a + b
        elif token == "-":
            return a - b
        elif token == "*":
            return a * b
        else:
            return int(a / b)