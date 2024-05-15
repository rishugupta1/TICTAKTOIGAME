
def CompTurn(board):
    best_score = -float('inf')
    best_move = None

    # Loop through all possible moves
    for i in range(9):
        if board[i] == 0:
            # Make the move
            board[i] = 1  # Assuming computer's mark is 1
            # Calculate the score for this move
            score = minimax(board, False)
            # Undo the move
            board[i] = 0
            # If this move is better than the current best move, update best move
            if score > best_score:
                best_score = score
                best_move = i

    # Make the best move
    board[best_move] = 1  # Assuming computer's mark is 1
def minimax(board, is_maximizing):
    # Check if the game is over
    winner = analyseboard(board)
    if winner != 0:
        return winner

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = 1  # Assuming computer's mark is 1
                score = minimax(board, False)
                board[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = -1  # Assuming player's mark is -1
                score = minimax(board, True)
                board[i] = 0
                best_score = min(score, best_score)
        return best_score






def analyseboard(board):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in win_combinations:
        if board[combo[0]] != 0 and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]  # Return the winning player's mark
    return 0

def ConstBoard(board):
    print("The current state of the board:\n\n")
    for i in range(0, 9):
        if i != 0 and i % 3 == 0:
            print("\n")
        if board[i] == 0:
            print("_ ", end=" ")
        elif board[i] == 1:
            print("O ", end=" ")
        elif board[i] == -1:
            print("X ", end=" ")

print("\n\n")


def User1Turn(board):
    pos = int(input("Enter 'X' pos [1-9]: "))
    if pos < 1 or pos > 9:
        print("Invalid position! Position must be between 1 and 9.")
        return

    if board[pos - 1] != 0:
        print("Wrong move! That position is already taken.")
        return

    board[pos - 1] = -1
    return board

def User2Turn(board):
    pos = int(input("Enter '0' pos [1-9]: "))
    if pos < 1 or pos > 9:
        print("Invalid position! Position must be between 1 and 9.")
        return

    if board[pos - 1] != 0:
        print("Wrong move! That position is already taken.")
        return

    board[pos - 1] = 1
    return board








def main():
  choice=input("Enter 1  for single Player or 2 for Multi-Player : ")
  choice=int(choice)
  board=[0,0,0,0,0,0,0,0,0,0]
  if(choice==1):
    print("Computer '0' vs You 'X':\n")
    player=input("Enter to play 1st('1') or 2nd('2):")
    player=int(player )
    for i in range (0,9):
      if (analyseboard(board)!=0):
        break
      if((i+player)%2==0):
        CompTurn(board)
      else:
        ConstBoard(board)
        User1Turn(board)

  else:
    for i in range (0,9):
      if (analyseboard(board)!=0):
       break
      if i%2==0:
        ConstBoard(board)
        User1Turn(board)
      else:
         ConstBoard(board)
         User2Turn(board)

  if(analyseboard(board)==0):
    print("Draw")
  elif(analyseboard(board)==-1):
    print("player :1 , has won")
  else:
    print("player :2 , has won")



main()