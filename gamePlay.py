#!python3

"""
playing tic-tac-toe
"""
import random, x01_data, x02_display, x03_winner

def setupHuman():
    print("Tic Tac Toe\n")
    human = input("X or O: ")
    inkorect = True
    while inkorect:
        if human == "X" or human == "O" or human == "x" or human == "o":
            inkorect = False
            break
        human = input("Enter X or O: ")
    if human == 'o':
        human = 'O'
    elif human == 'x':
        human = 'X'
    return (human,1)

def setupAi(human):
    if human[0] == 'O':
        ai = 'X'
    else:
        ai = 'O'
    return (ai,2)

def firstOrSecond():
    ForS = input("Do you want to go first or second: ")
    while True:
        if ForS == "first":
            return 1
        elif ForS == 'second':
            return 2
        ForS = input("Enter first or second: ")

def target(player,board):
    if player[1] == 1:
        x02_display.displayString(board)
        humanTarget = int(input("Enter your target number: "))
        inkorect = True
        while inkorect:
            if x01_data.read(humanTarget,board) != None:
                print("7 8 9\n4 5 6\n1 2 3\n")
                print("Square tacken")
                x02_display.displayString(board)
                humanTarget = int(input("Enter your new target number: "))
            else:
                inkorect = False
        return humanTarget
    elif player[1] == 2:
        aiTarget = int(random.randrange(1,10))
        inkorect = True
        while inkorect:
            if x01_data.read(aiTarget,board) != None:
                aiTarget = random.randrange(1,10)
            else:
                inkorect = False
        return aiTarget


def play(player1,player2):
    board = [0,0,0,0,0,0,0,0,0]
    print("board corodents\n7 8 9\n4 5 6\n1 2 3\n")
    winner = None
    while winner == None:
        player1Target = target(player1,board)
        x01_data.write(player1Target,board,player1[0])
        if 0 not in board and  x03_winner.whoWins(board) == None:
            winner == 0
            break
        elif  x03_winner.whoWins(board) != None:
            winner = x03_winner.whoWins(board)
            break
        player2Target = target(player2,board)
        x01_data.write(player2Target,board,player2[0])
        if 0 not in board and  x03_winner.whoWins(board) == None:
            winner == 0
        else:
            winner = x03_winner.whoWins(board)
    x02_display.displayString(board)
    print(winner)
    if winner == player1[0] and player1[1] == 1:
        print("You win!!")
    elif winner == player2[0] and player2[1] == 1:
        print("You win!!")
    elif winner == None:
        print("tie")
    else:
        print("You loss")

if __name__ == "__main__":
    human = setupHuman()
    ai = setupAi(human)
    spot = firstOrSecond()
    if spot == 1:
        play(human,ai)
    elif spot == 2:
        play(ai,human)