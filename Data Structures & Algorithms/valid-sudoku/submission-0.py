class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        m = len(board[0])
        sqaure_size = 3

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(n):
            for j in range(m):
                val = board[i][j]
                
                if val == ".":
                    continue

                if val in rows[i]:
                    return False
                
                if val in cols[j]:
                    return False
                
                if val in squares[(i // sqaure_size, j // sqaure_size )]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                squares[(i // sqaure_size, j // sqaure_size )].add(val)

        
        return True

"""

row = {0:(1, 2, 3)}
"""