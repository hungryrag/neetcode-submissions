class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        pref[0] = nums[0]
        suff[n-1] = nums[n-1]

        for i in range(1, n):
            # print(i)
            pref[i] = pref[i-1] * nums[i]
            suff[n-i-1] = suff[n-i] * nums[n-i-1]

        # print(f"pref: {pref}")
        # print(f"suff: {suff}")

        res =  [0] * n
        for i in range(0, n):
            if i == 0:
                res[i] = suff[i+1]
            elif i == n-1:
                res[i] = pref[i-1]
            else:
                res[i] = pref[i-1] * suff[i+1]
        return res