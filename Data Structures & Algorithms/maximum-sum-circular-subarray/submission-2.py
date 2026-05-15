class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        curr_max = 0
        global_max = nums[0]

        curr_min = 0
        global_min = nums[0]

        total = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            global_max = max(global_max, curr_max)

            curr_min =  min(curr_min + num, num)
            global_min = min(global_min, curr_min)
            
            total += num
        
        circular_max = total - global_min
        if circular_max == 0:
            return global_max

        return max(global_max, circular_max)