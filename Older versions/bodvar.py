"""
--------------------------
Piece encoding:
--------------------------

0000 -> 0 -> Empty square
0001 -> 1 -> Black stone
0010 -> 2 -> White stone
0100 -> 4 -> Stone marker
0111 -> 7 -> Offboard square
1000 -> 8 -> Liberty marker

0101 -> 5 -> Black stone marked
0110 -> 6 -> White stone marked

"""

# Stones
BLACK = 1
WHITE = 2
MARKER = 4
OFFBOARD = 7
LIBERTY = 8

# Board size
BOARD_SIZE = 9
MARGIN = 2
BOARD_RANGE = BOARD_SIZE + MARGIN

# GO board
board=[
    7,7,7,7,7,7,7,7,7,7,7,
    7,0,0,0,0,0,0,0,0,0,7,
    7,0,0,0,0,0,0,0,0,0,7,
    7,0,8,1,8,0,0,6,0,0,7,
    7,0,0,8,2,0,0,0,0,0,7,
    7,0,0,0,0,0,0,0,0,0,7,
    7,0,0,0,0,0,0,5,0,0,7,
    7,0,0,0,0,0,0,0,0,0,7,
    7,0,0,0,0,0,0,0,0,0,7,
    7,0,0,0,0,0,0,0,0,0,7,
    7,7,7,7,7,7,7,7,7,7,7
]


# ASCII representation on stones
pieces='.o#  bw +'

def print_board():
    # Loop over board rws
    for row in range(BOARD_RANGE):
        # loop over board columns
        for col in range(BOARD_RANGE):
            # initalize the square
            square = row * BOARD_RANGE + col
            # print(square)
            
            # print the rank
            if col == 0 and (0 < row < 10): 
                print(' '+ str(10 - row), end='')
            
            # initalize stone 
            stone=board[square]
            
            # print board squares content
            print(pieces[stone] + ' ', end='')
        print()
    # print notation
    print('    a b c d e f g h j\n')
print_board()