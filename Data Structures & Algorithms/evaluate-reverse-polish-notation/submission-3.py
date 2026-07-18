class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack.append(int(tokens[0]))
        # i = 0
        n = len(tokens)
        operators = ["+", "-", "*", "/"]
        for i in range(1,n):
            if (tokens[i] not in operators):
                stack.append(int(tokens[i]))
            else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    if (tokens[i] == "+"):
                        res = num1 + num2
                    if (tokens[i] == "-"):
                        res = num2 - num1
                    if (tokens[i] == "*"):
                        res = num1 * num2
                    if (tokens[i] == "/"):
                        res = int(float(num2 / num1))
                    
                    stack.append(int(res))
                
        return int (stack[0])
                



        