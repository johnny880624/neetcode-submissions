class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv}
        for num in tokens:
            if num in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = ops[num](int(num2), int(num1))
                stack.append(num3)
            else:
                stack.append(num)
        
        return int(stack[0])
                    
            