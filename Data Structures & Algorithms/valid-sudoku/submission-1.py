class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            rows = []
            cols = []
            box = []

            for col in range(len(board[row])):
                if board[row][col] != '.':
                    rows.append(board[row][col])
                    
                if board[col][row] != '.':
                    cols.append(board[col][row])
            
            for boxR in range(3):
                for boxC in range(3):
                    boxRow = row // 3 * 3 + boxR
                    boxCol = row % 3 * 3 + boxC
                    if board[boxRow][boxCol] != '.':
                        box.append(board[boxRow][boxCol])

            if len(rows) != len(set(rows)) or len(cols) != len(set(cols)) or len(box) != len(set(box)):
                return False

        return True

                


