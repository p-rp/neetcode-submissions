class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num : seq_len
        seen = defaultdict(int)

        longest_seq = 1

        for num in nums:

            if seen[num]  == 0:
                seen[num] += seen[num-1] + seen[num+1] + 1

                seen[num - seen[num-1]] = seen[num]
                seen[num + seen[num+1]] = seen[num]

                longest_seq = max(longest_seq, seen[num])

        return longest_seq


"""
max = 0 -> 1
seen {2:3, 20:1, 4:3, 10:1, 3:3, 5:4}
"""