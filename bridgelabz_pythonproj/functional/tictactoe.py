'''
/**********************************************************************************
* Purpose: Write a Program to play a Cross Game or Tic­Tac­Toe Game. Player 1 is
* the Computer and the Player 2 is the user. Player 1 take Random Cell that is the
* Column and Row.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 24-12-2018
*
***********************************************************************************/
'''
import random
print("this is tic tac toe game")
print("enter integer values between 1-9 for your move")
print("player 1 is computer and player 2 is user")
print("'o' will represent computer and 'x' will represent user")

board = [' ' for i in range(10)]  # initialise board with range 10 just to add extra space


def insert_letter(letter, pos):  # to add x or o at particular position
    board[pos] = letter


def free_space(pos):  # read or check empty tile
    return board[pos] == ' '


def print_board(board):  # print board of 9x9
    print("  |  | ")
    print(board[1] + ' ' + board[2] + ' ' + board[3] + ' ')  # represents tile numbers
    print("  |  | ")
    print("---------")
    print("  |  | ")
    print(board[4] + ' ' + board[5] + ' ' + board[6] + ' ')
    print("  |  | ")
    print("---------")
    print("  |  | ")
    print(board[7] + ' ' + board[8] + ' ' + board[9] + ' ')
    print("  |  | ")


def winner(b, l):  # take value from tile and store it in common variable
    return (b[1] == l and b[2] == l and b[3] == l or
            b[4] == l and b[5] == l and b[6] == l or  # if the values are equal then it is winning condition
            b[7] == l and b[8] == l and b[9] == l or
            b[1] == l and b[4] == l and b[7] == l or
            b[2] == l and b[5] == l and b[8] == l or
            b[3] == l and b[6] == l and b[9] == l or
            b[1] == l and b[5] == l and b[9] == l or
            b[3] == l and b[5] == l and b[7] == l)


def player_move():  # player move
    run = True  # while player is playing
    while run:
        move = input("select between 1-9: ")  # select between 1-9 as board have 9 tiles
        try:
            move = int(move)  # converting string value in integer
            if 0 < move < 10:
                if free_space(move):
                    run = False  # after entering move players turn will stop
                    insert_letter('x', move)  # insert x on players move
                else:
                    print("this is occupied")  # if already occupied

            else:
                print("invalid number")  # if number is not in range of 1 to 9

        except ValueError:
            print("type integer")  # if user enter string value


def computer_move():
    possible_move = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['o', 'x']:  # possible letters on board
        for i in possible_move:  # possible moves can be empty or 'o'
            board_copy = board[:]  # board[:] copy the board in variable
            board_copy[i] = let
            if winner(board_copy, let):  # check winning condition
                move = i  # if move is winning move then select move
                return move

    corner = []  # create corner array which store corner tiles
    for i in possible_move:
        if i in [1, 3, 7, 9]:  # corner tiles
            corner.append(i)  # place computer move of corner tile

    if len(corner) > 0:
        move = select_random(corner)  # select random corner tile
        return move

    if 5 in possible_move:  # if winning tile is middle tile 5 then computer will go for 5
        move = 5
        return move

    edge = []  # edge array
    for i in possible_move:
        if i in [2, 4, 6, 8]:  # edge tiles
            edge.append(i)

    if len(edge) > 0:  # select non empty edge randomly
        move = select_random(edge)
        return move


def select_random(li):  # select randomly from corner array or edge array and store array in li
    ln = len(li)  # length of li
    r = random.randrange(0, ln)  # from range 1 to ln select random number for computer move
    return li[r]


def full_board(board):  # check whether all tiles are occupied
    if board.count(' ') > 1:  # if any of the tile is empty then board is not full
        return False
    else:
        return True


def main():  # main code to execute tic tac toe
    print_board(board)  # print the board
    while not (full_board(board)):  # when board is not full

        if not (winner(board, ('x'))):  # if user is not winner then computer will play
            move = computer_move()
            if move == 0:  # if no moves left then print  tie game
                print("tie")
            else:
                insert_letter('o', move)  # if not then insert computer move
                print("computer move: ", move)
            print_board(board)  # print updated board

        else:
            print("user won")
            break

        if not (winner(board, ('o'))):
            player_move()  # player move
            print_board(board)  # print updated board after player move

        else:
            print("computer won")
            break

    if full_board(board):  # if board is full and no winning condition is satisfied
        print("tie")  # then print tie


main()

