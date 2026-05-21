from functools import lru_cache
class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def dfs(val):
            

            if val == 0:
                return 0
            
            min_coin = math.inf

            for coin in coins:
                diff = val - coin
                if diff >= 0:
                    min_coin = min(min_coin, dfs(diff)+1)
        
            
            return min_coin

        res = dfs(amount)
        if res == math.inf:
            return -1

        return res


"""

         12
  11       7          2
10 6 1     
     0
"""