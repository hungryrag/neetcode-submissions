class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        i=0
        for num in nums:
            val = target-num
            if val in hm:
                return sorted([i, hm.get(val)])

            hm[num]=i
            i += 1

        return [-1, -1]
        