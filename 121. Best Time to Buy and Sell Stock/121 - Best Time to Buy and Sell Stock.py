class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=None
        profit=0
        for i in range(len(prices)):
            if(i==0):
                low=prices[i]
            elif(prices[i]<=low):
                low=prices[i]
            else:
                if(prices[i]-low>profit):
                    profit=prices[i]-low
            
        return profit