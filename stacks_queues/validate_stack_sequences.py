class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        popLen = len(popped)
        i=0

        for val in pushed:
            stack.append(val)
            while stack and i<popLen and stack[-1] == popped[i]:
                i+=1
                stack.pop()
        return stack == []
