class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        current_subarray_sum=nums[0]
        maxResult=nums[0]

        for i in range(1,len(nums)):
            current_subarray_sum=max(nums[i],current_subarray_sum + nums[i])
            maxResult=max(maxResult,current_subarray_sum)

        return maxResult


# 예시 실행
nums = []
a = Solution()
print(a.maxSubArray(nums))


# def maxSubArray(self, nums: list[int]) -> int:
    
#     # 2차원 리스트 초기화
#     sub = [[0] * len(nums) for _ in range(len(nums))]
#     maxResult = float('-inf')  # 최대값 초기화

#     for i in range(len(nums)):
#         for j in range(i, len(nums)):  # j는 i보다 크거나 같아야 함
#             if i == j:
#                 sub[i][j] = nums[i]  # 같은 인덱스면 자기 자신
#             else:
#                 sub[i][j] = sub[i][j-1] + nums[j]  # 이전 합에 nums[j] 더하기

#             if sub[i][j] > maxResult:  # 최대값 갱신
#                 maxResult = sub[i][j]
    
#     return maxResult