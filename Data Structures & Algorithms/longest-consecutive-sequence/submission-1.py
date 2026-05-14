class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()

        curr_length = 1
        max_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
                
            if nums[i-1] == nums[i] - 1:
                curr_length += 1
                max_length = max(max_length, curr_length)
            else:
                curr_length = 1
        return max_length