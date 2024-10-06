from typing import List

class Solution:
    def nextPermutation(self, nums):
        n = len(nums) 

        # Step 1: Find the break point:
        ind = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # If break point does not exist:
        if ind == -1:
            # reverse the whole array:
            nums.reverse()
            return nums

        # Step 2: Find the next greater element and swap it with arr[ind]:
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 3: reverse the right half:
        nums[ind+1:] = reversed(nums[ind+1:])

        return nums

nums=[]
a=Solution()
print(a.nextPermutation(nums))