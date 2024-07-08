class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
                if nums[i] % 3 == 1:
                    cnt+=1
                elif nums[i] % 3 == 2:
                    cnt+=1
                
        return cnt

nums = [1, 2, 3, 4]       
a = Solution()
result = a.minimumOperations(nums)
print(result)  
