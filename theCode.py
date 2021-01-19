#board 1 is our sample unsolved sudoku

board1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]

userentry=[[0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0]]

resetlist=[[7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]

#the function that lets the users correct their last entered digit of sudoku when they are impor ting their own
def correction(i,j):
    if j == 0 and i > 0:
        command = input(f"enter the correct number for row {i - 1} and column{7}")
        if not command.isnumeric():
            print("wrong entry, u entered a \"non numeric\" or a \"minus number\" entry!!")
            correction(i,j)
        elif 9<int(command) :
            print("wrong entry, the number gotta be between 0_9")
            correction(i, j)
        else: userentry[i-1][7]= int(command)


    elif j > 0:
        command = input(f"enter the correct number for row {i} and column{j - 1}")
        if not command.isnumeric():
            print("wrong entry, u entered a \"non numeric\" or a \"minus number\" entry!!")
            correction(i, j)
        elif 9 < int(command) :
            print("wrong entry, the number gotta be between 0_9")
            correction(i, j)
        else:
            userentry[i][j - 1] = int(command)
    for l in range(0, 9):
        if l == 3 or l == 6:
            print(" ")
        print(userentry[l][0:3], " ", userentry[l][3:6], " ", userentry[l][6:9])
#going to main menu and reseting the solved sample(we reset it cuz its possible that in last steps the sample sudoko is solved)
def mainmenu():
    for i in range(0, 9):
        for j in range(0, 9):
            board1[i][j] = resetlist[i][j]
    for i in range(0, 9):
        for j in range(0, 9):
            userentry[i][j] = 0

    command=input("""welcome to omid's sudoku solver! :)
see a sample sudoku and answer  > enter "1" 
enter a sudoku to solve         > enter "2" """)
    print("_______________________________________________________________________")
    if command=="1":
        for l in range(0, 9):
            if l == 3 or l == 6:
                print(" ")
            print(board1[l][0:3], " ", board1[l][3:6], " ", board1[l][6:9])
        print("----------------------------")
        put(board1)
    elif command=="2":
        entering(userentry)

# checking the users entery in every step they are entering some command or digits
def commandcheck(i,j,userentry):

    if j!=0 or i!=0 :
        print("enter \"cor\" to correct the last entry")
    command=input(f'''
enter \"main\" to go back to mainmenu)\nor enter the row {i} and column {j} of the sudoku which u want it to get solved''')
    print("_______________________________________________________________________")
    if command == "cor":
        correction(i,j)
        commandcheck(i,j,userentry)

    elif command == "main":
        print(" ")

        mainmenu()
    elif not command.isnumeric():
        print("wrong entry, u entered a \"non numeric\" or a \"minus number\" entry!!")
        commandcheck(i,j,userentry)
    elif  int(command) >9:
        print("wrong entry! the number gotta be between 0-9")
        commandcheck(i,j,userentry)
    else:
        userentry[i][j]=int(command)





#when the user is entering their sudoko
def entering(userentry):
    for i in range (9):
        for j in range(9):
            commandcheck(i,j,userentry)
            for l in range(0, 9):
                if l == 3 or l == 6:
                    print(" ")
                print(userentry[l][0:3], " ", userentry[l][3:6], " ", userentry[l][6:9])
            print("----------------------------")
    command=input("ok, the border is completed, check the numbers u enterd and type any thing to start solving it\n or type ''wrong'' to reenter the border" )
    if command=="wrong":
        for i in range(0, 9):
            for j in range(0, 9):
                userentry[i][j] = 0
        entering(userentry)
    else:
        put(userentry)

#when the program is solving the problem, it tries with numbers in range of 0,9 to check if the sudoku rules can be still saticfied with the entered number
def ifok(table,n,row,col):


    # rows
    for i in range(0,9):
        if table[row][i]==n :
            return False
    #cols
    for i in range(0,9):
        if table[i][col]==n  :
            return False
    # boxes
    boxx = row // 3
    boxy = col // 3
    for i in range (3 * boxx, 3*boxx + 3):
        for j in range (3 * boxy, 3*boxy + 3):
            if table[i][j] == n :
                return False

    return True
#puting the checked number into the table and going to the next empty square in our sudoku, using recursion
# in here, every time that we enter a digit in our table, we go to ifok function to find the next possible digit for our current empty square
#if we cant find any, we go one step back to our last entered digit in our last square and try the rest of the digits which still arent tried in range of 0,9

def put(table):

    for i in range(0,9):
        for j in range(0,9):
            if table[i][j]==0:
                for n in range(1,10):
                    if ifok(table,n,i,j):
                        table[i][j]=n
                        put(table)
                        table[i][j] = 0


                return

    for l in range(0,9):
        if l == 3 or l == 6:
            print(" ")
        print(table[l][0:3]," ",table[l][3:6]," ",table[l][6:9])
    print("----------------------------")
    mainmenu()



mainmenu()
