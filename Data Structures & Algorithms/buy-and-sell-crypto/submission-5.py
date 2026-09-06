class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for l in range(len(prices)):
            r = len(prices)-1
            while l<=r:
                if prices[r]-prices[l]>max:
                    max = prices[r]-prices[l]
                r -= 1
        return max
