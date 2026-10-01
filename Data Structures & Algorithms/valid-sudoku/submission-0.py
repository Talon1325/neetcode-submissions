class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = 9
        for row in range(l):
            seen = set()
            for i in range(l):
                if board[row][i] != "." and board[row][i] in seen:
                    return False
                else:
                    seen.add(board[row][i])
        for col in range(l):
            seen = set()
            for i in range(l):
                if board[i][col] != "." and board[i][col] in seen:
                    return False
                else:
                    seen.add(board[i][col])
        for square in range (9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] != "." and board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True


