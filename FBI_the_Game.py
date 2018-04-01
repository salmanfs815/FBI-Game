# global variables and constants
dataFile = 'FBI_the_Game_Data_2.txt'
hiddenBone = " X " # this is how hidden bones are represented in the 2D backyard array
foundBone = " B " # this is how bones that the player has found are represented in the backyard

def createBackyard(width, height):
    """
    This function initializes an empty 'backyard'.
    It takes as parameters the width and height of the desired backyard.
    It returns the empty backyard (grid of dots).
    """
    row = int(height)
    column = int(width)
    backyard = [ [ ' . ' for i in range(column) ] for j in range(row)]
    return backyard

def drawBackyard(backyard, numOfBones, lengthOfBones):
    """
    This function draws the backyard in its current state.
    It takes as parameters the backyard which is to be drawn along with
    the number of bones buried in it and the length of each bone.
    Hidden bones are represented in the backyard as " X " and are displayed
    to the user as empty spaces, " . ".
    Bones that have been found are represented in the backyard as " B " and
    are displayed as such.
    The column and row numbering are generated dynamically using the backyard.
    This function doesn't return anything
    """
    
    height = len(backyard)
    width = len(backyard[0])

    print("\nThere are %i bones, each are %i cells long, buried in this backyard! Can you find them?" %(numOfBones, lengthOfBones))
    
    columnNumbers = "" # initialize variable

    # Dynamically generate column numbering
    for i in range(len(backyard[0])):
        if i == 0:
            print(' ', end='')
        if i < 10:
            columnNumbers += (str(i) + '  ')
        else:
            columnNumbers += (str(i) + ' ')

    # print the backyard, hide hidden bones, add row numbering
    rowNumber = 0
    for aRow in range(height):
        if aRow == 0:
            print(columnNumbers)
        for l in range(width):
            if backyard[aRow][l] == hiddenBone:
                print(" . ", end='')
            else:
                print(backyard[aRow][l], end='')
        print('', rowNumber)
        rowNumber +=1

def coordinateSelection(backyardWidth, backyardHeight):
    """
    This function takes and validates input from the user to
    select which position they want to search for the bone.
    It takes the width and height of the backyard as parameters.
    Valid data is: 2 digits separated by a space that represent <row> <column>.
    "-1" is to quit and all other input data is invalid.
    """
    print("\nTo do so, please, enter the row and the column number of a cell in which you suspect a bone is buried \n(e.g., 0 3 if you suspect that part of a bone is buried on the first row at the 4th column).")

    userInput = input("Enter -1 to quit : ")

    # check if user gave no input
    if len(userInput) == 0:
        print("***You have not entered anything. You need to enter a valid row and the column number!\n")
        return "invalid"
    # check if input is a string
    elif userInput.isalpha():
        print("***You have entered %s. You need to enter a valid row and the column number!\n" %userInput)
        return "invalid"
    else:
        # split input (string) into list
        userInput = userInput.split()
        # check if user wants to quit
        if int(userInput[0]) == -1:
            return "quit"
        # check if user entered only 1 value
        elif len(userInput) == 1:
            print("***You have entered only 1 value. You need to enter a valid row and the column number!\n")
            return "invalid"
        # check if user's input is out of range
        elif int(userInput[0]) >= backyardHeight :
            print("You needed to enter a row and column number of a cell that is within the backyard!\n")
            return "invalid"
        # check if user's input is out of range
        elif int(userInput[1]) >= backyardWidth:
            print("You needed to enter a row and column number of a cell that is within the backyard!\n")
            return "invalid"
        # check if user's input is out of range
        elif (int(userInput[0]) < 0) or (int(userInput[1]) < 0):
            print("You needed to enter a row and column number of a cell that is within the backyard!\n")
            return "invalid"
        # return valid data
        else:
            row = int(userInput[0])
            column = int(userInput[1])            
            return [row, column]

def checkForHiddenBones(backyard, bonesHidden):
    """
    This function checks if there are any more hidden bones in the backyard.
    It takes the backyard and Boolean bonesHidden variable as parameters.
    It returns True if there are still bones to find and False if all bones have been found.
    """
    hiddenBoneCells = 0
    for i in range(len(backyard)):
        if hiddenBone in backyard[i]:
            hiddenBoneCells += 1
    if hiddenBoneCells > 0:
        return True # there are still hidden bones
    else: return False # all bones have been found

###*** MAIN ***###

print("Welcome to Fast Bone Investigation (FBI) the game. \nIn this game, we dig out bones from Mrs. Hudson's backyard!")

# open data file in read mode
dataFileR = open(dataFile, 'r')

# read the first line of the data file and save the data as integers in a list
line1 = dataFileR.readline().strip().split()

# assign data from the 1st line of the file as variables
backyardWidth = int(line1[0])
backyardHeight = int(line1[1])
numOfBones = int(line1[2])
lengthOfBones = int(line1[3])

# create backyard, height and width taken from data file line 1
backyard = createBackyard(backyardWidth, backyardHeight)

# store all data from data file into a list as integers
allBonesData = []
for bone in range(1, numOfBones+1):
    bone = dataFileR.readline().strip().split()
    for i in bone:
        allBonesData.append(int(i))

# using previously created list, mark all bone coordinates with 'hiddenBone'
index = 0
while index < len(allBonesData):
    backyard[allBonesData[index]][allBonesData[index+1]] = hiddenBone
    index += 2

# display the backyard for the player
drawBackyard(backyard, numOfBones, lengthOfBones)

coordinateChoice = "" # initialize variable

# bonesHidden is True if any segment of any bone is still hidden
bonesHidden = True

while (bonesHidden == True) and (coordinateChoice != "quit"):

    # get user input for position selection
    coordinateChoice = coordinateSelection(backyardWidth, backyardHeight)

    # if user chose to quit, then quit (skip following statements)
    if coordinateChoice != "quit":
    
        if coordinateChoice != "invalid":
        
            row = coordinateChoice[0]
            column = coordinateChoice[1]
            # check if user found a bone segment
            if backyard[row][column] == hiddenBone:
                backyard[row][column] = foundBone
                print("\n****HIT!!!!****\n")
            # inform user if they have re-entered a coordinate where a bone is
            elif backyard[row][column] == foundBone:
                print("\nYou have already HIT this position!\n")
            # inform user that they have missed
            else:
                print("\n****OOPS! MISSED!****\n")

        # display backyard to user
        drawBackyard(backyard, numOfBones, lengthOfBones)

    # check if there are more hidden bones
    bonesHidden = checkForHiddenBones(backyard, bonesHidden)

    # print finish message if all bones have been found
    if bonesHidden == False:
        print("\n***** WOW !!! You found ALL the bones! *****\n")

print("\nWasn't it fun! Bye!")
