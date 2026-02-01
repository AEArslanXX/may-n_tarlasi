import random

#tahtayı hazırlama
mine_num = 10
board = [[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]]
board_len = len(board)

#listeler 
row_numbers = list(range(0,board_len))
col_numbers = list(range(0,board_len))

#satır , sütunları ve pozisyonu öğrenme öğrenme
def row(n):
    if n <= 0:
        return False
    n -= 1
    return board[n]
def col(n):
    if n <= 0:
        return False
    n -= 1
    column = []
    for i in range(0,board_len):
        column.append(board[i][n])
    return column
def pos(r,c):
    if r < 1 or c < 1:
        return False
    return (r-1)*board_len+c

#mayınları yerleştirme
def place_mines(n=mine_num):
    if n == 0:
        return False
    choose_row = random.choice(row_numbers)
    choose_col = random.choice(col_numbers)
    if(board[choose_row][choose_col] != 1):
        board[choose_row][choose_col] = 1
    else:
        place_mines()
    n -= 1
    board[choose_row][choose_col] = 1
for n in range(mine_num):
    place_mines()
for i in board:
    print(i)
