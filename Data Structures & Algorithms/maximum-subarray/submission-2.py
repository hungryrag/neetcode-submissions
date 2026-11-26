class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        globalMax = maxSum
        for i in range(1, len(nums)):
            maxSum = max(maxSum + nums[i], nums[i])
            globalMax = max(maxSum, globalMax)

        return globalMax