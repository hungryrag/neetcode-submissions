class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        tmp = []
        for n in nums:
            if n == 0:
                cnt += 1
                continue
            tmp.append(n)

        for i in range(0, cnt):
            tmp.append(0)       
        # print(tmp)
        for i in range(0, len(nums)):
            nums[i] = tmp[i]
        

        
        