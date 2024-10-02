class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 두 개의 반복문을 통해 모든 조합을 확인
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # 두 수의 합이 target과 같으면 인덱스를 반환
                if nums[i] + nums[j] == target:
                    return [i, j]
