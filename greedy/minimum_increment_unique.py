class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minMove = 0
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                incValue = nums[i-1] + 1
                minMove += incValue - nums[i]
                nums[i] = incValue
        return minMove
