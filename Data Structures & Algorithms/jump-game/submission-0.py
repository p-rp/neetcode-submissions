class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reached = n-1

        for i in range(n-2, -1, -1):
            if nums[i] + i >= reached:
                reached = i
        
        return reached == 0

"""

 0 1 2 3 4 
[1,2,0,1,0]
-------i
---------r

"""