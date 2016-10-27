#(c) Copyright by github user : yunaranyancat
#Project TICTACTOE

board = ['1','2','3','4','5','6','7','8','9'] #Total number of box in TicTacToe
marker = False #True if one of the player wins
number = 1 #Board number
player1 = 0
player2 = 0
pl1 = 'X'
pl2 = 'Y'
winnerX = 'X'
winnerY = 'Y'
def printboardbegin():
    for x in board:
        if (int(x)>3):
            if (4 <= int(x) <= 6):
                if (int(x) == 6):
                    print(int(x), end='\n')
                else:
                    print(int(x), end='     ' ) #4-6
            else:
                if int(x) == 9:
                    print(int(x), end='\n')
                else:
                    print(int(x), end='     ') #7-9
        else:
            if int(x)==3:
                print(int(x), end='\n')
            else:
                print(int(x), end='     ')#1-3


def begingame():
    print('The game begins!')
    print('Player 1 turn')

def boardreval(): #validity of board number
    valvalid = input('Value invalid, please insert a new value=  ')
    return int(valvalid)



def tst(v): #if board is not empty and exist then insert X(player1) or insert Y(player2)2
    if v in range(1,10):
        global number
        if board[v-1]!='X' and board[v-1]!='Y':
            print('Done!')
            if player1<=player2:
                changeboardtoX(v)
            else:
                changeboardtoY(v)
        else:
             a = int(input('Board number full, please enter a new board number =  '))
             tst(a)
    else:
        tst(boardreval())


def player_input():
    global player1
    global player2
    num=1
    if player1<=player2:
        num = input ('Player 1: What board number you want to insert your X? =  ') #input given is in string
        a = tst(int(num))
        player1+=1

    else:
        num = input('Player 2: What board number you want to insert your Y? =  ')
        b = tst(int(num))
        player2+=1

def changeboardtoX(n):
    board[n-1] = pl1

def changeboardtoY(n):
    board[n-1] = pl2

def fullboard(board):
    for x in board:
        if str(x)!='X' and str(x)!='Y':
            return False
            break
    return True


def printnewboard():
        print(' ' + board[0] + '|' + board[1] +'|' + board[2], end='')
        print('') #if we dont put this sh&t, then it will be 1 2 3 4 5 6 7 8 9 because of end='' at the top of this statement
        print(' ' + board[3] + '|' + board[4] + '|' + board[5],end='')
        print('')
        print(' ' + board[6] + '|' + board[7] + '|' + board[8], end='')
        print('')
        #elif x == board[5]:
        #    print(x,'\n')
        #elif x==board [8]:
         #   print(x,'\n')

'''def printnewboard():
    for x in board:
        if x == board[2] or x == board[5] or x == board[8]:
           print(' ' +str(x) + '|')

        #elif x == board[5]:
        #    print(x,'\n')
        #elif x==board [8]:
         #   print(x,'\n')
        else:
            print(' ' + str(x) + '|' + ' ', end='     ')
    print(end='')'''

def checkwinner(n):
    if n!='X':
        print('Player 2 wins!')
    else:
        print('Player 1 wins!')


def checkgame():
    global marker
    if board[0]==board[1]==board[2]:
        print("We've got a winner!")
        marker = True
        checkwinner(board[0])
        return marker
    elif board[3]==board[4]==board[5]:
        print("We've got a winner!")
        marker = True
        checkwinner(board[3])
        return marker
    elif board[6]==board[7]==board[8]:
        print("We've got a winner!")
        marker = True
        checkwinner(board[6])
        return marker
    elif board[0]==board[3]==board[6]:
        print("We've got a winner!")
        marker = True
        checkwinner(board[0])
        return marker
    elif board[1]==board[4]==board[7]:
        print("We've got a winner!")
        marker = True
        checkwinner(board[1])
        return marker
    elif board[2]==board[5]==board[8]:
        print("We've got a winner!")
        marker = True
        checkwinner(board[2])
        return marker
    elif board[0]==board[4]==board[8]:
        print("We've got a winner!")
        marker = True
        checkwinner(board[0])
        return marker
    elif board[2]==board[4]==board[6]:
        print("We've got a winner!")
        marker = True
        checkwinner(board[2])
        return marker
    else:
        marker=fullboard(board)
        if marker == True:
            print("Itsaaaa TIE!")
            return marker
        else:
            print("Game is still going")
            marker=False
            return marker

def restartgame():
    global board
    global number
    global player1
    global player2
    global pl1
    global pl2
    global winnerX
    global winnerY
    global marker
    ans = input('Would you like to restart the game? Y/N =  ')
    if (ans=='Y'):
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Total number of box in TicTacToe
        marker = False  # True if one of the player wins
        number = 1  # Board number
        player1 = 0
        player2 = 0
        pl1 = 'X'
        pl2 = 'Y'
        winnerX = 'X'
        winnerY = 'Y'
        printboardbegin()
        begingame()
        while (marker == False):
            player_input()
            printnewboard()
            checkgame()
    elif (ans=='N'):
        print('Thank you for playing this game ^^')
    else:
        restartgame()

printboardbegin()
begingame()#Print the board at the initial phase
while(marker==False):
    player_input()
    printnewboard()
    checkgame()

restartgame()


while(marker==False):
    player_input()
    printnewboard()
    checkgame()
