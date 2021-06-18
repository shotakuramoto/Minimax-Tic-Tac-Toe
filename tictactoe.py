#Assignment 1
#AI Tic Tac Toe. We use minimax algorithm to optimise the best possible hand for each player

#this is the library used in python
import sys
#Global variable that helps us to identify which is which in the follwoing program
Max = 'x'
Min = 'o'
#when it is true, it is max turn when it is false, it is min turn
#File name is stored here, and the board that is temporary there for the early termination
Turn = 1
FileName = ""
Index = -1
temporary_board = ['-','-','-','-','-','-','-','-','-']

#printing the TicTacToe into the text file
#following the format of the board state and the output
def output_txt(TicTac, number):
    out_str = ''.join(TicTac)
    #concatenate the string for the output
    out_str = out_str + ' ' + str(number)

    f = open(FileName,"a")
    f.write(out_str+"\n")
    f.close()

#this function checks whether the board has any space in the board
def check_fill(board):
    count = 0
    #This counts the number of the space
    for i in board:
        if i == '-':
            count = count + 1
    
    #when the count is 9, there is not space in the board
    #so return false, no more space
    else:
        return count 

# Max = 'x'
# Min = 'o'
##This function tells which turns is it in the game
def whose_turn(board):
    #This counts the number of the min and max
    count_max = 0
    count_mini = 0
    global Turn

    for i in board:
        if i == Max:
            count_max = count_max + 1
        if i == Min:
            count_mini = count_mini + 1

    # we return true when it is Max's o turn
    if count_max == count_mini: 
        Turn = 1

    #Return when it is Min turn
    if count_max > count_mini:
        Turn = 0
    
    return Turn

#this function checks whether the board is in a situation where
#either palyer win the match
def Win_Lose(TicTac):
    #There are 8 possible ways of either players winning the game
    #we check it here

    #now we check for the diagonal
    #lefttop to right bottom
    if (TicTac[0]==TicTac[4]==TicTac[8]!='-'):
        if (TicTac[0]==Max):
            return 1
        if (TicTac[0]==Min):
            return -1

    #righttop to leftbottom
    if (TicTac[2]==TicTac[4]==TicTac[6]!='-'):
        if (TicTac[2]==Max):
            return 1
        if (TicTac[2]==Min):
            return -1

    #This we check the row, three in a row
    #use the if statment that three characters would be the same
    ##Error Here
    if (TicTac[0]==TicTac[1] ==TicTac[2]!='-'):
        if (TicTac[0]==Max):
            return 1
        if (TicTac[0]==Min):
            return -1
    
    if (TicTac[3]==TicTac[4]==TicTac[5]!='-'):
        if (TicTac[3]==Max):
            return 1
        else:
            return -1

    if (TicTac[6]==TicTac[7]==TicTac[8]!='-'):
        if (TicTac[6]==Max):
            return 1
        else:
            return -1
    
    #This we check the column, three in a column
    if (TicTac[0]==TicTac[3]==TicTac[6]!='-'):
        if (TicTac[0]==Max):
            return 1
        if (TicTac[0]==Min):
            return -1
    
    if (TicTac[1]==TicTac[4]==TicTac[7]!='-'):
        if (TicTac[1]==Max):
            return 1
        if (TicTac[1]==Min):
            return -1
    
    if (TicTac[2]==TicTac[5]==TicTac[8]!='-'):
        if (TicTac[2]==Max):
            return 1
        if (TicTac[2]==Min):
            return -1

    #when it is no win or lose, we return 0, that still indicates game is draw
    #or havent decided
    return 0

#This function concatenates the best possible board from the list and print it out on the terminal
def string_terminal(TicTac):
    string = ""
    for i in range(9):
        string = string + TicTac[i]
    print(string)

#We prepeare a empty board that we can find the winning pattern for the early termination
def erase_content():
    for i in range(9):
        temporary_board[i] = '-'

#this function will count the number of times where x or o will win the game from the current board
def Find_ms_os(num):
    count_win = 0
    
    if (num == 1):
        if (temporary_board[0]==temporary_board[4]==temporary_board[8]=='x'):
            count_win = count_win + 1
        if (temporary_board[2]==temporary_board[4]==temporary_board[6]=='x'):
            count_win = count_win + 1
        if (temporary_board[0]==temporary_board[1] ==temporary_board[2]=='x'):
            count_win = count_win + 1
        if (temporary_board[3]==temporary_board[4]==temporary_board[5]=='x'):
            count_win = count_win + 1
        if (temporary_board[6]==temporary_board[7]==temporary_board[8]=='x'):
            count_win = count_win + 1
        if (temporary_board[0]==temporary_board[3]==temporary_board[6]=='x'):
            count_win = count_win + 1
        if (temporary_board[1]==temporary_board[4]==temporary_board[7]=='x'):
            count_win = count_win + 1
        if (temporary_board[2]==temporary_board[5]==temporary_board[8]=='x'):
            count_win = count_win + 1
    elif (num == 0):
        if (temporary_board[0]==temporary_board[4]==temporary_board[8]=='o'):
            count_win = count_win + 1
        if (temporary_board[2]==temporary_board[4]==temporary_board[6]=='o'):
            count_win = count_win + 1
        if (temporary_board[0]==temporary_board[1] ==temporary_board[2]=='o'):
            count_win = count_win + 1
        if (temporary_board[3]==temporary_board[4]==temporary_board[5]=='o'):
            count_win = count_win + 1
        if (temporary_board[6]==temporary_board[7]==temporary_board[8]=='o'):
            count_win = count_win + 1
        if (temporary_board[0]==temporary_board[3]==temporary_board[6]=='o'):
            count_win = count_win + 1
        if (temporary_board[1]==temporary_board[4]==temporary_board[7]=='o'):
            count_win = count_win + 1
        if (temporary_board[2]==temporary_board[5]==temporary_board[8]=='o'):
            count_win = count_win + 1
    
    return count_win

#now we have to run a function that returns the
#E(s)
#So E(S) is the difference in number of possible winning route between x and o
#So we fill up all the space with x or o and space and check the number of winning cases
def return_Es(TicTac):
    #we start filling all the space and x's on the empty board
    for i in range(9):
        if (TicTac[i]!='o'):
            temporary_board[i]='x'

    #then this will get the M(s)
    MS = Find_ms_os(1)
    erase_content()

    #we start filling all the space and o's on the empty board
    for i in range(9):
        if (TicTac[i]!='x'):
            temporary_board[i]='o'

    #then this will get the M(s)
    OS = Find_ms_os(0)
    erase_content()

    return (MS - OS)

#Minimax function with early termination
#The base case is calling that function calcualtes the ES
#apart from that it is the same
def Mini_Max_Total(choice, Turn,TicTac, alpha, beta, depth):

    #Only for early termination
    #depth has to decrease by one, everytime minimax is called
    #and when the depth is equal to 0, return the E(S) value
    if (choice == 5):
        temp = depth
        depth=int(temp)-1
        if (depth == 0):
            return return_Es(TicTac)

        #This checks the board state
        result=Win_Lose(TicTac)

        #if Max win, the result will be 1
        if (result==1):
            return return_Es(TicTac)
        #if Min win, the resutl will be -1
        if (result==-1):
            return return_Es(TicTac)
        #we also return Draw when there is no more space to move the pawn
        count = 0
        for i in range(9):
            if (TicTac[i] == '-'):
                count = 1
        #when there is no more space left, we return 0.
        #this represent that the board is draw
        if (count==0):
            return return_Es(TicTac)
    

    #For normal minimax and alpha beta pruning
    else:
        #When it reaches the leaf node, aka win, lose, or all space filled
        #base case activated
        #This checks the board state
        result=Win_Lose(TicTac)

        #if Max win, the result will be 1
        if (result==1):
            return result

        #if Min win, the resutl will be -1
        if (result==-1):
            return result

        #we also return Draw when there is no more space to move the pawn
        count = 0
        for i in range(9):
            if (TicTac[i] == '-'):
                count = 1

        #when there is no more space left, we return 0.
        #this represent that the board is draw
        if (count==0):
            return 0

    #This code runs when it Turn is True, that implies max turn
    if (Turn==1):

        #we set a value that can be the highest hypothetically
        res = -100

        for char in range(9):
            #By marking different space, and using minimax algorithm,
            # we find the best possible solution
            if (TicTac[char]=='-'):
                TicTac[char]='x'
                
                #find the larger value between the best value
                #you ever obtained and the new value
                comp = Mini_Max_Total(choice, 0, TicTac, alpha, beta, depth)

                #Pruning can happne in AB pruning and early termination code
                if (choice == 4 or choice == 5):
                    #This is the best value
                    if (comp > res):
                        res=comp
                    #finding the alpha value
                    if (res > alpha):
                        alpha = res
                    
                    #possible pruning occuring
                    if alpha >= beta:
                        output_txt(TicTac, comp)
                        TicTac[char] = '-'
                        return res
                
                elif (choice == 0):
                    if (comp>res):
                        res=comp
                
                output_txt(TicTac, comp)
                TicTac[char]='-'

        return res

    #Min Turn
    else:
        
        #Min will always try to choose the lowest possible number
        #Therefore the variable needs to be initialised to the highest number possible
        res=100

        for char in range(9):
            if (TicTac[char]=='-'):
                TicTac[char]='o'

                #find the larger value between the best value
                #you ever obtained and the new value
                comp = Mini_Max_Total(choice, 1, TicTac, alpha, beta, depth)

                if (choice == 4 or choice == 5):
                    if (comp<res):
                        res=comp
                    #finding the alpha value
                    if (res < beta):
                        beta = res
                    
                    #possible pruning occuring
                    if alpha >= beta:
                        output_txt(TicTac, comp)
                        TicTac[char] = '-'
                        return res
                
                elif (choice == 0):
                    if (comp<res):
                        res=comp                   

                output_txt(TicTac, comp)
                TicTac[char]='-'

        return res

#This is the function that calls the minimax algorithm
#Also, update the coordination of the best possible 
def Best_Func(choice, TicTac, Turn, depth):
    bestVal_max= -1000
    bestVal_min = 1000

    alpha = -10
    beta = 10

    #We travel through all the cells, and find the best possible move calling the minimax function
    for char in range(9):

        #We find the sapce in the board and we start calling the minimax function
        if (TicTac[char] =='-'):
            Turn= whose_turn(TicTac)
            #As we have two players, we prepare for Min and Max
            if (Turn == 1):
                TicTac[char] = 'x'
                #Minimax called, and get the best possible value from this route
                Turn= 0

                temp = 0
                #Selecting the parameters of the minimax by the choice value
                #One function can do three different role by changing the choice value
                if (choice == 4):
                    compare=Mini_Max_Total(choice, Turn,TicTac,alpha, 1000, depth)
                    output_txt(TicTac, compare)
                    temp = compare
                elif (choice == 5):
                    compare = Mini_Max_Total(choice, Turn, TicTac, alpha, 1000, depth)
                    output_txt(TicTac, compare)
                    temp = compare
                elif (choice == 0):
                    compare = Mini_Max_Total(choice, Turn, TicTac, alpha, beta, depth)
                    output_txt(TicTac, compare)
                    temp = compare
                
                TicTac[char] = '-'

                #Just Alpha Beta Pruning and early termination
                #We have to constantly update the alpha value or beta value in o turn
                if (choice == 4 or choice == 5):
                    if (temp > bestVal_max):
                        bestVal_max=temp
                        Index = char 
                    
                    if (temp > alpha):
                        alpha = temp
                
                #In normal turn, we just check the best possbile value
                else:
                    if (temp > bestVal_max):
                        bestVal_max=temp
                        Index = char

            elif (Turn == 0):
                TicTac[char] = 'o'
                #Minimax called, and get the best possible value from this route
                Turn= 1
                
                temp = 0
                if (choice == 4):
                    compare=Mini_Max_Total(choice, Turn,TicTac,-1000, beta, depth)
                    output_txt(TicTac, compare)
                    temp = compare
                elif (choice == 5):
                    compare = Mini_Max_Total(choice, Turn, TicTac, -1000, beta, depth)
                    output_txt(TicTac, compare)
                    temp = compare
                elif (choice == 0):
                    compare = Mini_Max_Total(choice, Turn, TicTac, alpha, beta, depth)
                    output_txt(TicTac, compare)
                    temp = compare

                TicTac[char] = '-'

                if (choice == 4 or choice == 5):
                    if (temp < bestVal_min):
                        bestVal_min=temp
                        Index = char 
                    
                    if (temp < beta):
                        beta = temp
                
                else:
                    if (temp < bestVal_min):
                        bestVal_min=temp
                        Index = char

    #This is the output function                      
    Turn= whose_turn(TicTac)
    if (Turn == 1):
        TicTac[Index] = Max
        string_terminal(TicTac)
    else:
        TicTac[Index] = Min
        string_terminal(TicTac)

    return

##The main driver code
mayprune = len(sys.argv)
Input = sys.argv[1]
File = sys.argv[2]
TicTac = list(Input)
FileName = File

#we check the input, and when there is no more space, we terminate the program
left = check_fill(TicTac)
if (left == 0):
    sys.exit()

#when alpha beta pruning
if (mayprune == 4):
    Best_Func(4, TicTac, Turn, 0)
#When early termination as well
elif (mayprune == 5):
    depth = sys.argv[4]
    Best_Func(5, TicTac, Turn, depth)
else:
    Best_Func(0, TicTac, Turn, 0)