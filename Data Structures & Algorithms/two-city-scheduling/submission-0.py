class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        costs.sort(key=lambda x: x[0]-x[1],)

        total = sum(cost[0] for cost in costs[:n])
        total += sum(cost[1] for cost in costs[n:])
        
        return total

"""

[[10,20],[30,200],[400,50],[30,20]]

    -10     -170    350      10

  [30,200] [10,20] [30,20] [400,50]  

"""