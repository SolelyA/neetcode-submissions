class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for c in tokens:
            if c not in operators:
                stack.append(c)
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if c == "+":
                    stack.append(str(op1 + op2))
                elif c == "-":
                    stack.append(str(op1 - op2))
                elif c == "*":
                    stack.append(str(op1 * op2))
                elif c == "/":
                    if (op1 / op2) < 0:
                        stack.append(str(math.ceil((op1 / op2))))
                    else:
                        stack.append(str(math.floor((op1 / op2))))
                        
        return int(stack[-1])
