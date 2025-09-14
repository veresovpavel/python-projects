def print_cells():
    cells_1 = cells[0] + " " + cells[1] + " " + cells[2]
    cells_2 = cells[3] + " " + cells[4] + " " + cells[5]
    cells_3 = cells[6] + " " + cells[7] + " " + cells[8]
    print(f"""
---------
| {cells_1} |
| {cells_2} |
| {cells_3} |
---------""")


def three_in_a_row(list_win):
    x = list_win[0] - 1
    y = list_win[1] - 1
    z = list_win[2] - 1
    if cells[x] == cells[y] == cells[z]:
        w = cells[x]
    else:
        w = False
    return w


def empty():
    state = 'ok'
    for elem in cells:
        if elem == ' ':
            state = 'Game not finished'
        elif elem == '_':
            state = 'Game not finished'
    return state


def impossible():
    check = 'ok'
    count_x = 0
    count_o = 0
    for i in range(9):
        if cells[i] == 'X':
            count_x += 1
        elif cells[i] == 'O':
            count_o += 1
    if abs(count_x - count_o) > 1:
        check = 'Impossible'
    return check


def winner_check():
    state_win = "Unknown"
    win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    get_x = 'i'
    get_o = 'i'
    row = 'i'
    for el in win_list:
        row = three_in_a_row(el)
        if row == 'X':
            get_x = 'X'
        if row == "O":
            get_o = 'O'
    if get_x != get_o:
        if get_x == 'X':
            state_win = 'X wins'
        elif get_o == 'O':
            state_win = 'O wins'
    if get_x == 'X' and get_o == 'O':
        state_win = 'Draw'
    elif get_x != 'X' and get_o != 'O':
        if empty() == 'ok':
            state_win = 'Draw'
    if state_win != 'X wins':
        if state_win != 'O wins':
            if empty() != 'ok':
                if state_win == 'Draw':
                    state_win = 'Impossible'
                else:
                    state_win = empty()
    if impossible() != 'ok':
        state_win = impossible()
    return state_win


def user_input(letter):
    while True:
        print('Enter the coordinates')
        user_sells = input().split()
        if user_sells[0].isdigit() and user_sells[1].isdigit():
            user_sell_1 = int(user_sells[0])
            user_sell_2 = int(user_sells[1])
            if (0 < user_sell_1 < 4) and (0 < user_sell_2 < 4):
                user_cell = (user_sell_2 - 1) + (user_sell_1 - 1) * 3
                if cells[user_cell] != "X" and cells[user_cell] != "O":
                    cells[user_cell] = letter
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


cells = list(" " for i in range(0, 9))
print_cells()
turn = "X"
while winner_check() == "Game not finished":
    if turn == "X":
        user_input(turn)
        print_cells()
        turn = "O"
    elif turn == "O":
        user_input(turn)
        print_cells()
        turn = "X"
State = winner_check()
print(State)
