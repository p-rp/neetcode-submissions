class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # subarray count
        subarrays = 0

        for i in range(len(nums)):
            sum_ = 0
            for j in range(i, len(nums)):
                sum_ += nums[j]
                if sum_ == k:
                    subarrays += 1

        return subarrays