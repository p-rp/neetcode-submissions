class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(cost) > sum(gas):
            return -1

        starting = 0
        fuel = 0

        for i in range(len(gas)): 
            fuel += gas[i]
            fuel -= cost[i]

            if fuel < 0:
                starting = i+1
        
        return starting