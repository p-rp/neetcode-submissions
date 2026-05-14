class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profits += diff
        
        return profits


"""
[5 4 3 2 3 4 5 10]
      p
   l

profits = 0 -> 4

"""