class Solution:
    List = list

    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        prof = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            prof = max(prof, prices[r] - prices[l])
        return prof


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
