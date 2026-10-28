class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i=0
        while(i<len(s)):
            if s[i] != ")":
                stack.append(s[i])
            else:
                stackReverse = []
                while(stack[-1] != "("):
                    stackReverse.append(stack.pop())
                stack.pop()
                stack.extend(stackReverse)
            i+=1
        return "".join(stack)

                
