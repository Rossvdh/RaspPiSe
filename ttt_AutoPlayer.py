# Re-writing the auto TTT player functions in python
# Ross van der Heyde VHYROS001
# 1 August 2018.

import random

def copyboard(board):
    copy = []

    for row in board:
        copy.append(list(row))

    return copy

def getAvailableMoves(board):
    moves = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == blank:
                moves.append((row, col))

    return moves

def shuffle(movesAndScores):
    for i in range(len(movesAndScores)-1, 0, -1):
        rand = random.randint(i+1)
        movesAndScores[i], movesAndScores[rand] = movesAndScores[rand], movesAndScores[i]


def getBestMove(board, colour):
    moves = getAvailableMoves(board)
    movesAndScores = []

    for move in moves:
        newBoard = copyboard(board)
        newBoard[move[0]][move[1]] = colour

        result = getWinner(board)
        score = 0
        if result == "tie":
            score = 0
        else if result == colour:
            score = 1
        else:
            otherColour = green if colour == red else green
            nextMove = getBestMove(newBoard, otherColour)
            score -= nextMove()

        if score == 1:
            return (move, score)

        movesAndScores.append((move, score))

    shuffle(movesAndScores)

    movesAndScores.sort(key=(lambda m: m[1]))

    return movesAndScores[0]
