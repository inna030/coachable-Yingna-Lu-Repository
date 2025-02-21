class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        preSign = '+'
        stack = []
        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                elif preSign == '/':
                    stack.append(math.trunc(stack.pop() / num))
                preSign = i  # Moved inside
                num = 0      # Moved inside
        return sum(stack)
