class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        print(nums)
        indiceFound = []
        for val in range(len(nums)):
            if nums[val] == target:
                indiceFound.append(val)
        return indiceFound
