class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stacks = []
        for token in tokens:
            if token == "+":
                a,b = stacks.pop(),stacks.pop()
                stacks.append( a + b)
            elif token == "-":
                a,b = stacks.pop(),stacks.pop()
                stacks.append( b - a)
            elif token == "*":
                a,b = stacks.pop(),stacks.pop()
                stacks.append( a * b)
            elif token == "/":
                a,b = stacks.pop(),stacks.pop()
                stacks.append( int(float (b)/a))
            else :
                stacks.append(int(token))
        return stacks[0]
            
