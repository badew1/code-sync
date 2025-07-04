class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}

        for i in range(len(nums)):
            if target - nums[i] not in numdict:
                numdict[nums[i]] = i
            else:
                return [i, numdict[target - nums[i]]]

        return