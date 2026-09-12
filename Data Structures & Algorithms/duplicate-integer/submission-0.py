class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_uni = []
        for n in nums:
            if n not in num_uni:
                num_uni.append(n) 
            else:
                return True
        return False