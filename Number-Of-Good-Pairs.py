class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        goodPairsFound = 0

        for i in range(len(nums)):
            for j in range(len(nums)):

                if nums[i] == nums[j] and i < j:

                        goodPairsFound += 1

        return goodPairsFound
