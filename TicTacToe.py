human, comp = 'x', 'o'

def isMoveLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def checkForWin(board, player):
    winning_states = [[board[row][0], board[row][1], board[row][2]]
                      for row in range(3)]
    winning_states += [[board[0][col], board[1][col], board[2][col]]
                       for col in range(3)]
    winning_states += [[board[0][0], board[1][1], board[2][2]]]
    winning_states += [[board[2][0], board[1][1], board[0][2]]]

    if [player, player, player] in winning_states:
        return True
    return False

def evaluate(board, player):
    val = 0

    if (checkForWin(board, player)):
        if player == comp:
            val = 10
        elif player == human:
            val = -10
    return val

def minmax(board, depth, isMax, player):
    score = evaluate(board, player)

    if score == 10:
        return score

    if score == -10:
        return score

    if isMoveLeft(board) == False:
        return 0

    if isMax:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = comp
                    best = max(best, minmax(board, depth + 1, not isMax, comp))
                    board[i][j] = '_'
        return best
    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = human
                    best = min(best, minmax(board, depth + 1, not isMax, human))
                    board[i][j] = '_'
        return best


def findBestMove(board):
    best_val = -1000
    best_move = ()

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = comp
                move_val = minmax(board, 0, False, comp)
                board[i][j] = "_"

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

moves = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}
def playHuman(board):
    move = ()
    
    while True:
        num = int(input("Enter your move (1-9): "))
        move = moves[num]
        if (board[move[0]][move[1]] == '_'):
            break
        else: print("Invalid move. Please try again")

    return move

def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def playTTT():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    printBoard(board)

    no_moves = 0
    win = False
    while (no_moves != 9):
        move = playHuman(board)
        print("User: ")
        board[move[0]][move[1]] = human
        # print(board)
        printBoard(board)
        print()
        no_moves += 1
        if checkForWin(board, human):
            win = True
            print("Human won!")
            break
        
        if (no_moves == 9):
            break

        print("Comp: ")
        move = findBestMove(board)
        board[move[0]][move[1]] = comp
        no_moves += 1
        printBoard(board)
        if checkForWin(board, comp):
            win = True
            print("Comp won!")
            break


    if win == False and no_moves == 9:
        print("Draw")

playTTT()
