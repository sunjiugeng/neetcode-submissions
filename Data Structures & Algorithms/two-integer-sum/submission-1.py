class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for idx, num in enumerate(nums): 
            balance = target - num
            if balance in index_dict:
                return [index_dict[balance], idx]
            else:
                index_dict[num] = idx
        return [-1, -1]