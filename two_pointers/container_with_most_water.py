class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        leftPos , rightPos = 0 , len(height)-1

        while leftPos < rightPos:
            area = (rightPos - leftPos) * min(height[leftPos],height[rightPos])
            maxArea = max(maxArea,area)

            if height[leftPos] < height[rightPos]:
                leftPos += 1
            else:
                rightPos -= 1
        return maxArea
