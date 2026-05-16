class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(val):

            if val in memo:
                return memo[val]

            if val == 0:
                return 0
            
            min_coins = math.inf

            for coin in coins:
                
                diff = val - coin

                if diff >= 0:
                    min_coins = min(dfs(diff)+1, min_coins)
            
            memo[val] = min_coins
            return min_coins


        min_coins = dfs(amount)
        if min_coins == math.inf:
            return -1
        return min_coins

"""
                12

    11          7               2
10  6  1      1  2             1 
    5   0     0                0
    0
"""