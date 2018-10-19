import random

def make_board():
    '''
    Create a game board in its initial state.
    The board is a dictionary mapping (row, column) coordinates
    (zero-indexed) to integers which are all powers of two (2, 4, ...).
    Exactly two locations are filled.
    Each contains either 2 or 4, with an 80% probability of it being 2.

    Arguments: none
    Return value: the board
    '''

    potential = []

    for i in range(4):
        for j in range(4):
            current = (i, j)
            potential.append(current)

    random.shuffle(potential)
    new = random.random()
    new2 = random.random()
    board = {}

    if new < 0.8:
        new = 2
    else:
        new = 4

    if new2 < 0.8:
        new2 = 2
    else:
        new2 = 4

    board[potential[0]] = new
    board[potential[1]] = new2

    return board

#
# Problem 3.2
#

def get_row(board, row_n):
    '''
    Return a row of the board as a list of integers.
    Arguments:
      board -- the game board
      row_n -- the row number

    Return value: the row
    '''

    assert 0 <= row_n < 4

    taken = {}

    for place in board:
        if place[0] == row_n:
            taken[place[1]] = board[place]

    obtain = []

    for i in range(4):
        if i in taken:
            obtain.append(taken[i])
        else:
            obtain.append(0)

    return obtain


def get_column(board, col_n):
    '''
    Return a column of the board as a list of integers.
    Arguments:
      board -- the game board
      col_n -- the column number

    Return value: the column
    '''

    assert 0 <= col_n < 4

    taken = {}

    for place in board:
        if place[1] == col_n:
            taken[place[0]] = board[place]

    obtain = []

    for i in range(4):
        if i in taken:
            obtain.append(taken[i])
        else:
            obtain.append(0)

    return obtain


def put_row(board, row, row_n):
    '''
    Given a row as a list of integers, put the row values into the board.

    Arguments:
      board -- the game board
      row   -- the row (a list of integers)
      row_n -- the row number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= row_n < 4
    assert len(row) == 4

    for place, number in enumerate(row):
        board[row_n, place] = number
        if board[row_n, place] == 0:
            del board[row_n, place]



def put_column(board, col, col_n):
    '''
    Given a column as a list of integers, put the column values into the board.

    Arguments:
      board -- the game board
      col   -- the column (a list of integers)
      col_n -- the column number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= col_n < 4
    assert len(col) == 4

    for place, number in enumerate(col):
        board[place, col_n] = number
        if board[place, col_n] == 0:
            del board[place, col_n]


#
# Problem 3.3
#

def make_move_on_list(numbers):
    '''
    Make a move given a list of 4 numbers using the rules of the
    2048 game.

    Argument: numbers -- a list of 4 numbers
    Return value: the list after moving the numbers to the left.
    '''

    assert len(numbers) == 4

    copy = []

    for value in numbers:
        if value != 0:
            copy.append(value)
    while len(copy) < 4:
        copy.append(0)

    index = 0
    merge = []

    while index < 4:
        if index < 3:
            if copy[index] == copy[index + 1]:
                merge.append(copy[index] * 2)
                index += 2
            else:
                merge.append(copy[index])
                index += 1
        else:
            merge.append(copy[index])
            index += 1

    while len(merge) < 4:
        merge.append(0)

    return merge


#
# Problem 3.4
#

def make_move(board, cmd):
    '''
    Make a move on a board given a movement command.
    Movement commands include:

      'w' -- move numbers upward
      's' -- move numbers downward
      'a' -- move numbers to the left
      'd' -- move numbers to the right

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    assert cmd in ['w', 'a', 's', 'd']

    if cmd == 'w':
        for i in range(4):
            current = get_column(board, i)
            new = make_move_on_list(current)
            put_column(board, new, i)

    elif cmd == 's':
        for i in range(4):
            current = get_column(board, i)
            current.reverse()
            new = make_move_on_list(current)
            new.reverse()
            put_column(board, new, i)

    elif cmd == 'a':
        for i in range(4):
            current = get_row(board, i)
            new = make_move_on_list(current)
            put_row(board, new, i)

    else:
        for i in range(4):
            current = get_row(board, i)
            current.reverse()
            new = make_move_on_list(current)
            new.reverse()
            put_row(board, new, i)


#
# Problem 3.5
#

def game_over(board):
    '''
    Return True if the game is over i.e. if no moves can be made on the board.
    The board is not altered.

    Argument: board -- the game board
    Return value: True if the game is over, else False
    '''

    if len(board) != 16:
        return False
    check = dict(board)

    make_move(check, 'w')
    if check != board:
        return False

    make_move(check, 'a')
    if check != board:
        return False

    make_move(check, 's')
    if check != board:
        return False

    make_move(check, 'd')
    if check != board:
        return False
    else:
        return True


#
# Problem 3.6
#

def update(board, cmd):
    '''
    Make a move on a board given a movement command.  If the board has changed,
    then add a new number (2 or 4, 90% probability it's a 2) on a
    randomly-chosen empty square on the board.  This function assumes that a
    move can be made on the board.

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    check = dict(board)
    make_move(check, cmd)

    if check == board:
        pass

    else:
        make_move(board, cmd)
        empty = []
        for i in range(4):
            for j in range(4):
                if (i, j) not in board:
                    empty.append((i, j))

        new = random.random()
        if new < 0.9:
            new = 2
        else:
            new = 4

        new_loc = random.choice(empty)
        board[new_loc] = new


### Supplied to students:

def display(board):
    '''
    Display the board on the terminal in a human-readable form.

    Arguments:
      board  -- the game board

    Return value: none
    '''

    s1 = '+------+------+------+------+'
    s2 = '| {:^4s} | {:^4s} | {:^4s} | {:^4s} |'

    print(s1)
    for row in range(4):
        c0 = str(board.get((row, 0), ''))
        c1 = str(board.get((row, 1), ''))
        c2 = str(board.get((row, 2), ''))
        c3 = str(board.get((row, 3), ''))
        print(s2.format(c0, c1, c2, c3))
        print(s1)

def play_game():
    '''
    Play a game interactively.  Stop when the board is completely full
    and no moves can be made.

    Arguments: none
    Return value: none
    '''

    b = make_board()
    display(b)
    while True:
        move = input('Enter move: ')
        if move not in ['w', 'a', 's', 'd', 'q']:
            print("Invalid move!  Only 'w', 'a', 's', 'd' or 'q' allowed.")
            print('Try again.')
            continue
        if move == 'q':  # quit
            return
        update(b, move)
        if not b:
            print('Game over!')
            break
        display(b)


#
# Useful for testing:
#

def list_to_board(lst):
    '''
    Convert a length-16 list into a board.
    '''
    board = {}
    k = 0
    for i in range(4):
        for j in range(4):
            if lst[k] != 0:
                board[(i, j)] = lst[k]
            k += 1
    return board

def random_game():
    '''Play a random game.'''
    board = make_board()
    display(board)
    while True:
        print()
        move = random.choice('wasd')
        update(board, move)
        display(board)
        if game_over(board):
            break
