class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = sorted(set(nums))
        # print(tmp)
        nums[:] = tmp
        # print(nums)
        return len(nums)