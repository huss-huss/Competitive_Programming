class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxOfSum = 0
        n = len(nums)
        for i in range(n//2):
            maxOfSum = max(maxOfSum,nums[i]+nums[n-i-1])
        return maxOfSum
