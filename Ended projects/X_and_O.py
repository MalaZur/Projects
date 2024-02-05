
ok = 1 # Крестики нолики
while ok == 1:
  board = [['*','*','*'],['*','*','*'],['*','*','*']]
  def pretty_print(board):
    for i in range(3):
      for o in range(15): print('-', end='')
      print()
      for j in range(3): print(end=f" |{board[i][j]}| " )
      print()
    for o in range(15): print('-', end='')
    print()

  def take_input(player_token):
    n = int(input(f"\nСтрока, в которую будет вствлен {player_token}: "))-1
    m = int(input(f"Столбец, в которую будет вствлен {player_token}: "))-1
    if n in range(0,3) and m in range(0,3): 
      if board[n][m] == '*': board[n][m] = player_token
      else: 
        print("Эта клетка уже занята!")
        take_input(player_token)
    else:
      print("Были введены неверные данные, повторите еще раз.")
      take_input(player_token)

  def check_win__in_rows(board,token):
    for row in board:
      check_row = True
      for element in row:
        if element != token: check_row = False
      if check_row: return True
    return False

  def check_win__in_columns(board,token):
    for i in range(3):
      check_column = True
      for j in range(3):
        if board[j][i] != token: check_column = False
      if check_column: return True
    return False

  def check_win_in_diog(board, token):
    if (board[0][0] == token and board[1][1] == token and board[2][2]) or (board[0][2] == token and board[1][1] == token and board[2][0]) == token: return True
    else: return False

  def count_x(board):
    x = 0
    for i in range(3):
      for j in range(3):
        if board[i][j] == 'X': x+=1
    return x

  def count_o(board):
    o = 0
    for i in range(3):
      for j in range(3):
        if board[i][j] == 'O': o+=1
    return o

  def is_win(token):
    if check_win__in_columns(board, token): return True
    if check_win__in_rows(board, token): return True
    if check_win_in_diog(board, token): return True
    return False

  print("Первыми ходят крестики: ")
  p1 = 'X'
  p2 = 'O'
  pretty_print(board)
  take_input(p1)
  pretty_print(board)
  for i in range(9):
    if i == 8:
      print("Ничья!")
      break
    if count_x(board)>count_o(board):
      take_input(p2)
      pretty_print(board)
      if is_win(p2): 
        print("Победа за вторым игроком (нолики)!")
        break
    else:
      take_input(p1)
      pretty_print(board)
      if is_win(p1): 
        print("Победа за первым игроком (крестики)!")
        break
  ok = int(input("Хотите ли сыграть еще раз?\n(1)-да, (0)-нет: "))