class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        cursum, maxsum = nums[0], nums[0]
        
        for i in range(1,len(nums)):
            cursum = max(cursum+nums[i],nums[i])
            maxsum = max(cursum, maxsum)

        return maxsum
