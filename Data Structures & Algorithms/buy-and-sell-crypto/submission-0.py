class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i, pricei in enumerate((prices)):
            for j in range(i,len(prices)):
                profit = prices[j] - pricei
                print("pricei",pricei,"prices[j]",prices[j], "profit===>",profit)

                if profit > 0 and profit > maxProfit:
                    print("maxProfit==>",profit)
                    maxProfit = profit
        return maxProfit