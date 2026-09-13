class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kFrequent = {}
        for num in nums:
            if num in kFrequent:
                kFrequent[num] += 1
            else:
                kFrequent[num] = 1
        return [sorted(kFrequent.items(), key=lambda item: item[1], reverse=True)[i][0] for i in range(k)]