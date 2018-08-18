# Module with some functions for Ball Maze
# Ross van der Heyde VHYROS001
# UNiversity of Cape Town Computer Science Honours
# 13 August 2018

# REVISED ASSIGNMENT

blu = [0,0,255]
red = [255,0,0]
gre = [0,255,0]
whi = [255,255,255]
ora = [255,200,0]
yel = [255,255,0]
blk = [0,0,0]

def readMaze(mazeFile):
    """Reads a maze layout, including start and end points from
    a text file."""
    #provide this function in its entirety?
    mazeFile = open(mazeFile)
    lines = mazeFile.readlines()
    mazeFile.close()

    #strip \n
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

    #extract start position
    start = lines[0].split(",")
    start = list(map(int, start))
    del lines[0]

    #extract end position
    end = lines[0].split(",")
    end = list(map(int, end))
    del lines[0]

    #extract maze layout
    maze = []
    for line in lines:
        arr = line.split(" ")
        for i in arr:
            if i == "b":
                #blank LED
                maze.append(blk)
            elif i == "w":
                #wall
                maze.append(blu)
            elif i == "h":
                #h for hole
                maze.append(red)
            else:
                #target LED
                maze.append(gre)

    return start, end, maze


def saveTime(time, mazeFileName):
    """Saves the given time to the file time.txt if the time
    is lowest than the current saved for for the current maze."""
    #read file to get current best time
##    print("opening file")
    fileName = "times.txt"
    file = open(fileName, "r")

    lines = file.readlines()
    file.close()
##    print("file read")
    
    mazeNumber = mazeFileName[4]
##    print("mazeNumber =", mazeNumber)

    file = open(fileName, "w")

    #write out and update best time if necessary
    for line in lines:
        if line[0] == mazeNumber:
            #extract time
            bestTime = float(line[3:-1])
##            print("best time:", bestTime)

            if time < bestTime:
                print(mazeNumber+": " + str(time)+"\n", file=file, end="")
            else:
                print(line, file=file, end="")
        else:
            print(line, file=file, end="")

    file.close()
    print("writing complete")
