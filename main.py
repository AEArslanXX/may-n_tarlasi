#kütüphaneler.
import math
import random
import os

#terminal temizleme.
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
clear()
#mayın satırı ve sütunu listeleri.
row_list = list(range(0,8))
col_list = list(range(0,8))
mine_positions = []
#oyun tahtası ve arkada çalışacak tahta.
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
back_board = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],     #arkada çalışacak olan tahta.
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]
def print_board(_board=board):
    for i in _board:
        print(i)

mine_number = 10
board_len = len(board)

#satır ve sütunları ful yazdırma , pozisyon bulma.
def write_full_row(row_number,board_=board): #1'den başlar sona kadar.
    if row_number < 1 or row_number > board_len:
        return False
    return board_[row_number-1]
def write_full_col(col_number,board_=board): #buda 1'den başlar sona kadar.
    if col_number < 1 or col_number > board_len:
        return False
    columns_list = []
    for i in range(board_len):
        columns_list.append(board_[i][col_number-1])
    return columns_list
def write_position(row_number,col_number,board_=board):
    if row_number < -1 or col_number < -1 or row_number > board_len or col_number > board_len:
        return False
    return (row_number-1)*board_len+col_number

#kaçıncı sütunda veya satırda bulunduğunu öğrenme.
def learn_row(position):
    if position < 1 or position > board_len**2:
        return False
    return math.ceil(position / board_len)
def learn_col(position):
    if position < 1 or position > board_len**2:
        return False
    if position % board_len == 0:
        return board_len
    return position % board_len

#random mayın yerleştiren fonksiyon.
def place_mines():
    packet = []
    row_position = random.choice(row_list)
    col_position = random.choice(col_list)
    packet.append(row_position)
    packet.append(col_position)
    if packet in mine_positions:
        place_mines()
    else:
        mine_positions.append(packet)
        #mayınları back_boarda yerleştirme.
        back_board[row_position][col_position] = 1

#etrafındaki kareleri tarayan fonksiyon.
def scan(position,board_=back_board):
    mines = []
    count_of_mines = int()
    position_row = learn_row(position) -1
    position_col = learn_col(position) -1

    if position == 1:
        mines.append(back_board[position_row][position_col+1]) #sağ
        mines.append(back_board[position_row+1][position_col+1]) #sağ alt çapraz
        mines.append(back_board[position_row+1][position_col]) #alt
    elif position == 8:
            mines.append(back_board[position_row+1][position_col]) #alt
            mines.append(back_board[position_row+1][position_col-1]) #sol alt çapraz
            mines.append(back_board[position_row][position_col-1]) #sol

    elif position == 55:
        mines.append(back_board[position_row-1][position_col]) #üst
        mines.append(back_board[position_row-1][position_col+1]) #sağ üst çapraz
        mines.append(back_board[position_row][position_col+1]) #sağ
    elif position == 64:
        mines.append(back_board[position_row-1][position_col]) #üst
        mines.append(back_board[position_row][position_col-1]) #sol
        mines.append(back_board[position_row-1][position_col-1]) #sol üst çapraz
    elif position_col == 0 and (position != 1 or position != 55):
        mines.append(back_board[position_row-1][position_col]) #üst
        mines.append(back_board[position_row-1][position_col+1]) #sağ üst çapraz
        mines.append(back_board[position_row][position_col+1]) #sağ
        mines.append(back_board[position_row+1][position_col+1]) #sağ alt çapraz
        mines.append(back_board[position_row+1][position_col]) #alt
    elif position_col == 7 and (position !=8 or position !=64):
        mines.append(back_board[position_row-1][position_col]) #üst
        mines.append(back_board[position_row+1][position_col]) #alt
        mines.append(back_board[position_row+1][position_col-1]) #sol alt çapraz
        mines.append(back_board[position_row][position_col-1]) #sol
        mines.append(back_board[position_row-1][position_col-1]) #sol üst çapraz
    elif position_row == 0 and (position != 1 or position != 8):
        mines.append(back_board[position_row+1][position_col+1]) #sağ alt çapraz
        mines.append(back_board[position_row+1][position_col]) #alt
        mines.append(back_board[position_row+1][position_col-1]) #sol alt çapraz
        mines.append(back_board[position_row][position_col-1]) #sol
        mines.append(back_board[position_row][position_col+1]) #sağ
    elif position_row == 7 and (position != 55 or position != 64):
        mines.append(back_board[position_row-1][position_col]) #üst
        mines.append(back_board[position_row-1][position_col+1]) #sağ üst çapraz
        mines.append(back_board[position_row][position_col+1]) #sağ
        mines.append(back_board[position_row][position_col-1]) #sol
        mines.append(back_board[position_row-1][position_col-1]) #sol üst çapraz
    else:
        mines.append(back_board[position_row-1][position_col]) #üst
        mines.append(back_board[position_row-1][position_col+1]) #sağ üst çapraz
        mines.append(back_board[position_row][position_col+1]) #sağ
        mines.append(back_board[position_row+1][position_col+1]) #sağ alt çapraz
        mines.append(back_board[position_row+1][position_col]) #alt
        mines.append(back_board[position_row+1][position_col-1]) #sol alt çapraz
        mines.append(back_board[position_row][position_col-1]) #sol
        mines.append(back_board[position_row-1][position_col-1]) #sol üst çapraz


    count_of_mines = mines.count(1)
    return [mines,count_of_mines]

#mayınlar yerleşti
for i in range(10):
    place_mines()

print_board(back_board)
print("")
print(scan(63))
