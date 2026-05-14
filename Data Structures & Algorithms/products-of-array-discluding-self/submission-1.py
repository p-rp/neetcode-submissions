class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = nums[0]
        suffix = nums[-1]

        res = [1] * n

        for i in range(1, n):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(n-2, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res


"""
[1  2  4  6]
 1  1  2  8     prefix
 48 24 6 1      suffix
 

"""