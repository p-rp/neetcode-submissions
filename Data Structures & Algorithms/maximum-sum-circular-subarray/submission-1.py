class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        curr_max = 0
        global_max = nums[0]

        curr_min = 0
        global_min = nums[0]

        total = 0

        for num in nums:
            curr_max += num
            global_max = max(global_max, curr_max)

            if curr_max < 0:
                curr_max = 0
            
            curr_min += num
            
            if num < curr_min:
                curr_min = num

            global_min = min(global_min, curr_min)
            
            total += num
        
        circular = total - global_min
        if circular == 0:
            return global_max

        return max(global_max, circular)