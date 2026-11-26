class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_max=0
        curr=prices[0]
        for i in range(1, len(prices)):
            local_max=0
            if prices[i] < curr:
                curr=prices[i]
            elif prices[i] > curr:
                local_max = prices[i] - curr
                
            global_max = max(global_max, local_max)

        return global_max
        