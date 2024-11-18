def is_safe(board, row, col):
   
    for i in range(row):
        if board[i][col] == 1:
            return False


    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row):
   
    if row >= len(board):
        return True

    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

        
            if solve_n_queens_util(board, row + 1):
                return True

            
            board[row][col] = 0

    return False


def solve_n_queens(n):
   
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0):
        print("No solution exists")
        return

    
    print_board(board)


def print_board(board):
    
    for row in board:
        for cell in row:
            print("Q" if cell == 1 else ".", end=" ")
        print()


solve_n_queens(8)
