class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if c == "+":
                    stack.append(op1 + op2)
                elif c == "-":
                    stack.append(op1 - op2)
                elif c == "*":
                    stack.append(op1 * op2)
                elif c == "/":
                    if (op1 / op2) < 0:
                        stack.append(math.ceil((op1 / op2)))
                    else:
                        stack.append(math.floor((op1 / op2)))
                        
        return int(stack[-1])
