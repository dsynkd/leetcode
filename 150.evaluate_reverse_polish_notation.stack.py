import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operator = ['+', '-', '*', '/']
        
        for token in tokens:
            if token == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
            elif token == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
            elif token == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                assert(op2 != 0)
                stack.append(math.trunc(op1 / op2))
            elif token == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            else:
                stack.append(int(token))
        
        assert(len(stack) == 1)
        return stack[0]