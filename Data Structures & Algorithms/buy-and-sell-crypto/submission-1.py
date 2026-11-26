class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_max=0
        curr=prices[0]
        for price in prices:
            global_max=max(price - curr, global_max)
            curr = min(curr, price)

        return global_max
        