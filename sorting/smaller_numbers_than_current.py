class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedNumbers = sorted(nums)
        indexs = {}
        results = []
        
        for val in range(len(nums)):
            if sortedNumbers[val] not in indexs:
                indexs[sortedNumbers[val]] = val
                
        for val in nums:
            results.append(indexs[val])
            
        return results
