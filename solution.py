def solvepart1():
    #read in data
    data = fileRead("input.txt")
    bricksFalling = []
    for row in data:
        splitRow = row.strip().split("~")
        num1 = splitRow[0].split(",")
        num2 = splitRow[1].split(",")
        num1 = tuple([ int(x) for x in num1 ])
        num2 = tuple([ int(x) for x in num2 ])
        bricksFalling.append((num1,num2))
    bricksFalling.sort(key = lambda brick: brick[0][2])

    #collapse bricks, and store necessary data to calculate safe disintigrations
    bricksSittingOn = {} #key is position of brick after landing, value is number of bricks it is sitting on
    bricksOnTopof = {} # same key, value is list of bricks on top of it
    maxHeight = 0
    for currBrick in bricksFalling:
        midair = True
        currZ = currBrick[0][2]
        sittingBricks = [] #bricks the current brick will land on
        while midair:
            if currZ == 1: #brick is on the ground
                midair = False
                break
            for stoppedBrick in bricksSittingOn.keys():
                if stoppedBrick[1][2] == currZ - 1: #stopped brick is below current brick in Z space
                    if (stoppedBrick[1][0] >= currBrick[0][0]) and (stoppedBrick[0][0] <= currBrick[1][0]): #stopped brick overlaps current brick in X space
                        if (stoppedBrick[1][1] >= currBrick[0][1]) and (stoppedBrick[0][1] <= currBrick[1][1]): #stopped brick overlaps current brick in Y space
                            midair = False
                            sittingBricks.append(stoppedBrick)
                        stoppedBrick[1] >= currBrick[0] or stoppedBrick[0] <= currBrick[1]
            if midair:
                currZ = currZ - 1
            
        newBrick = ((currBrick[0][0],currBrick[0][1], currZ), (currBrick[1][0],currBrick[1][1], currZ + ( currBrick[1][2] - currBrick[0][2] ) ))
        for brick in sittingBricks:
            bricksOnTopof[brick] = bricksOnTopof[brick] + (newBrick,)
        bricksSittingOn[newBrick] = len(sittingBricks)
        bricksOnTopof[newBrick] = tuple()

    #for each brick, calculate whether it can be disintigrated
    sum = 0
    for brick, aboveBricks in bricksOnTopof.items():
        if (len(aboveBricks) == 0):
            sum += 1
            continue
        valid = True
        for brick in aboveBricks:
            if (bricksSittingOn[brick] < 2):
                valid = False
                break
        if valid:
            sum += 1
    print(sum)

def solvepart2():
    #read in data
    data = fileRead("input.txt")
    bricksFalling = []
    for row in data:
        splitRow = row.strip().split("~")
        num1 = splitRow[0].split(",")
        num2 = splitRow[1].split(",")
        num1 = tuple([ int(x) for x in num1 ])
        num2 = tuple([ int(x) for x in num2 ])
        bricksFalling.append((num1,num2))
    bricksFalling.sort(key = lambda brick: brick[0][2])

    #collapse bricks, and store necessary data to calculate safe disintigrations
    global bricksSittingOn
    global bricksOnTopof
    bricksSittingOn = {} #key is position of brick after landing, value is number of bricks it is sitting on
    bricksOnTopof = {} # same key, value is list of bricks on top of it
    maxHeight = 0
    for currBrick in bricksFalling:
        midair = True
        currZ = currBrick[0][2]
        sittingBricks = [] #bricks the current brick will land on
        while midair:
            if currZ == 1: #brick is on the ground
                midair = False
                break
            for stoppedBrick in bricksSittingOn.keys():
                if stoppedBrick[1][2] == currZ - 1: #stopped brick is below current brick in Z space
                    if (stoppedBrick[1][0] >= currBrick[0][0]) and (stoppedBrick[0][0] <= currBrick[1][0]): #stopped brick overlaps current brick in X space
                        if (stoppedBrick[1][1] >= currBrick[0][1]) and (stoppedBrick[0][1] <= currBrick[1][1]): #stopped brick overlaps current brick in Y space
                            midair = False
                            sittingBricks.append(stoppedBrick)
                        stoppedBrick[1] >= currBrick[0] or stoppedBrick[0] <= currBrick[1]
            if midair:
                currZ = currZ - 1
            
        newBrick = ((currBrick[0][0],currBrick[0][1], currZ), (currBrick[1][0],currBrick[1][1], currZ + ( currBrick[1][2] - currBrick[0][2] ) ))
        for brick in sittingBricks:
            bricksOnTopof[brick] = bricksOnTopof[brick] + (newBrick,)
        bricksSittingOn[newBrick] = len(sittingBricks)
        bricksOnTopof[newBrick] = tuple()

    #for each brick, calculate whether it can be disintigrated
    sum = 0
    for brick in bricksOnTopof.keys():
        global bricksSittingOnTemp
        bricksSittingOnTemp = bricksSittingOn.copy()
        sum = sum + disintigrateBrickChain(brick) - 1
    print(sum)
    
# recursively calculate how many bricks would fall if a brick is disintigrated, target brick included
def disintigrateBrickChain(brick):
    if len(bricksOnTopof[brick]) == 0:
        return 1

    sum = 1
    for topBrick in bricksOnTopof[brick]:
        bricksSittingOnTemp[topBrick] = bricksSittingOnTemp[topBrick] - 1
        if bricksSittingOnTemp[topBrick] == 0:
            sum += disintigrateBrickChain(topBrick)
    return sum

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart2()