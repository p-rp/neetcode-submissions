class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        curr_sum = sum(cardPoints[:k])
        max_sum = curr_sum

        left = k-1
        right = len(cardPoints)-1

        for _ in range(k):
            curr_sum -= cardPoints[left]
            curr_sum += cardPoints[right]

            max_sum = max(max_sum, curr_sum)

            left -= 1
            right -= 1

        return max_sum