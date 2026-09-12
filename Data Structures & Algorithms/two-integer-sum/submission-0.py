class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n_1 in enumerate(nums):
            for j, n_2 in enumerate(nums[i + 1 :]):
                if n_1 + n_2 == target:
                    return [i, j + i + 1]
        