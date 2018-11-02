# Define globals
board = []
player = "X"
gameover = False

# Create a 2d Array for Board, based on user input. Also includes code to print board in a neat-looking way, and then returns the Board var. when called.
def setupboard():
	num = 1
	x = int(input("How large of a Tic-Tac-Toe game would you like to play? "))
	print ("Your chosen game size (x and y) is: ",x)
	for i in range(x):
		board.append([])
		for j in range(x):
			board[i].append(num)
			num += 1
	#board = [[1,2,3],
	#         [4,5,6],
	#         [7,8,9]]
	if x == 3:
		for i in board:
			for j in i:
				print(j, end = "  ")
			print()
	else:
		for i in board:
			print()
	return board

board = setupboard()

# For testing the board list, should return 1 if uncommented
#print(board[0][0])

# Checks for wins, defines row as the length of the board array. Subfunction check_win_row should look for wins in each row.
def checkwin(player):
	for x in len(board):
		check_win_row(x, board, player)
		check_win_col(x, board, player)
	check_win_diag_a(board, player)
	check_win_diag_b(board, player)
# Checks rows for wins
def check_win_row(rownum, daboard, player):
	winrow = True
	for col in len(board): 
		if board[rownum][col] != player:
			winrow = False
	return winrow

# Check column for wins
def check_win_col(colnum, daboard, player):
	wincol = True
	for row in len(board[0]): 
		if board[row][colnum] != player:
			wincol = False
	return wincol

# Check top-to-bottom diagonal for wins.
def check_win_diag_a(daboard, player):
	windiag_a = True
	for diag_a in len(board):
		if board[diag_a][diag_a] != player:
			windiag_a = False
	return windiag_a

# Check bottom-to-top diagonal for wins.
def check_win_diag_b(daboard, player):
	windiag_b = True
	for diag_b in len(board):
			if board[len(board)-diag_b][diag_b] != player:
				windiag_b = False
	return windiag_b

# Part of main Loop, select number from 2d Array
while(not gameover):
	try:
		play = int(input("Please pick a number on the board: "))
		if play > len(board)*len(board):
			print ("Your chosen number is invalid, please select another")
			#better try again... Return to the start of the loop
			continue
		if play <= 0:
			print ("Your chosen number is invalid, please select another")
			#better try again... Return to the start of the loop
			continue
		board[int(play/len(board))][play%len(board)-1] = player
	except ValueError:
		print ("Your chosen number is invalid, please select another")
		#better try again... Return to the start of the loop
		continue
	checkwin(player)
	if winrow == True:
		gameover = True
		print ("%s has won the game!" % player)
	elif wincol == True:
		gameover = True
		print ("%s has won the game!" % player)
	elif windiag_a == True:
		gameover = True
		print ("%s has won the game!" % player)
	elif windiag_b == True:
		gameover = True
		print ("%s has won the game!" % player)
	if player == "X":
		player = "Y"
		print ("It is now %s's turn." % player)
		continue
	else:
		player == "X"
		print ("It is now %s's turn." % player)
		continue
