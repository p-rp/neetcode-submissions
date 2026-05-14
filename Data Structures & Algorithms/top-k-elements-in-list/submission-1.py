class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums).items()
        min_heap = []
        for num, counts in freq:
            heapq.heappush(min_heap, (counts, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)


        return [num for _, num in min_heap]