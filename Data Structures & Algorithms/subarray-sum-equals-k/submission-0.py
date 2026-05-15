class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # subarray count
        subarrays = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                sum_ = sum(nums[i:j])
                if sum_ == k:
                    subarrays += 1

        return subarrays