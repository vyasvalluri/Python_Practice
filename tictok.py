#!/usr/bin/env python3
from os import system
board = [' ' for x in range(10)]

def insertletter(letter, pos):
    board[pos] = letter

def spaceIsfree(pos):
    return board[pos] == ' '

def isboardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(board, p):
    return (board[1] == p and board[2] == p and board[3] == p) or (board[4] == p and board[5] == p and board[6] == p) or (board[7] == p and board[8] == p and board[9] == p) or (board[1] == p and board[4] == p and board[7] == p) or (board[2] == p and board[5] == p and board[8] == p) or (board[3] == p and board[6] == p and board[9] == p) or (board[3] == p and board[5] == p and board[7] == p) or (board[1] == p and board[5] == p and board[9] == p)

def playermove():
    run = True
    while run:
        move = input("Please enter the position for 'X' in between 1 - 9 ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if(spaceIsfree(move)):
                    run = False
                    insertletter('X', move)
                else:
                    print("sorry this space is occupied")
            else:
                print("please enter valid position")
        except :
            print("Please enter valid position in between 1 - 9")

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    printboard(board)

    while not(isboardFull(board)):
        print("board not full ................")
        if not(isWinner(board , 'O')):
            playermove()
            printboard(board)
        else:
            print("sorry you loose!")
            break

        if not(isWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertletter('O' , move)
                print('computer placed an O on position' , move , ':')
                printboard(board)
        else:
            print("you win!")
            break
    print("board is full ...")
    if isboardFull(board):
        print("Tie game")




def printboard(board):
    system("clear")
    print("1    |2    |3   ")
    print("  " + board[1] + "  |  "+ board[2] + "  |   "+ board[3])
    print("     |     |    ")
    print("-----------------")
    print("4    |5    |6   ")
    print("  " + board[4] + "  |  "+ board[5] + "  |   "+ board[6])
    print("     |     |    ")
    print("-----------------")
    print("7    |8    |9   ")
    print("  " + board[7] + "  |  "+ board[8] + "  |   "+ board[9])
    print("     |     |    ")
    print()


while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break