class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = tuple(Counter(nums).items())
        freq = sorted(freq, key=lambda x: x[1], reverse=True)
        
        res = []

        for i in range(k):
            res.append(freq[i][0])

        return res