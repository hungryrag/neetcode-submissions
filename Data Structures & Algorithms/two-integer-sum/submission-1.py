class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            val = target-num
            if val in hm:
                return sorted([i, hm.get(val)])

            hm[num]=i

        return [-1, -1]
        