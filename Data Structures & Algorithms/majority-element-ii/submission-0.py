class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        freq = Counter(nums)

        res = []

        for (num, count) in freq.items():
            if count > n // 3:
                res.append(num)
        

        return res