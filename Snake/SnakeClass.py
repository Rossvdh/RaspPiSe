## A class represneting the Snake
# Ross van der Heyde VHYROS001
# UCT Computer Science Honours
# 17 July 2018

class SnakeClass:
    #class Attributes
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self):
        self.body = [[[4,1], SnakeClass.DOWN], [[4,0], SnakeClass.DOWN]]

        self.turningPoints = {}
        self.direction  = SnakeClass.DOWN

    def head(self):
        """Returns a tuple with co-ords of the head of the snake"""
        return tuple(self.body[0][0])

    def slither(self, food):
        """Moves the snake and food's co-ordinates, but does not set the LEDs
        in the matrix. Returns the result of the movement: "eat" when the
        snake eats the food and grows, "die" when the snake dies, or "none"
        when niether of those 2 happen."""
        result = "none"
        newSegment = []

        for i in range(len(self.body)):
            segment = self.body[i]
            #convert to tuple because a list can't be used as a
            #dictionary key
            pixel = tuple(segment[0])

            # check for turning point
            if pixel in self.turningPoints.keys():
                segment[1] = self.turningPoints[pixel]
                
                #if all points in the snake have passed, remove the TP
                if i == len(self.body)-1:
                    #being removed before the newly added segment gets to it
                    self.turningPoints.pop(pixel)

            if i == 0 and pixel == tuple(food):
                # the head eats the food
                # snake grows (new segment to be added)
                newSegment = list(self.body[len(self.body)-1])
                newSegment[0] = list(newSegment[0])
                self.body.append(newSegment)

                result = "eat"

            #move the snake
            dire = segment[1]
            if dire == SnakeClass.UP:
                segment[0][1] -=1
            elif dire == SnakeClass.LEFT:
                segment[0][0] -=1
            elif dire == SnakeClass.DOWN:
                segment[0][1] +=1
            else:
                segment[0][0] +=1

            #check if new position is in the snake
            snakePixels = self.getPixels()

            if snakePixels.count(segment[0]) > 1:
                result = "die"
                
        return result

    def changeDirection(self, newDirec):
        """Changes the direction of the Snake's movement"""
        if self.direction == SnakeClass.UP:
            if newDirec != SnakeClass.DOWN:
                self.direction = newDirec
                self.turningPoints[self.head()] = self.direction
        elif self.direction == SnakeClass.RIGHT:
            if newDirec != SnakeClass.LEFT:
                self.direction = newDirec
                self.turningPoints[self.head()] = self.direction
        elif self.direction == SnakeClass.DOWN:
            if newDirec != SnakeClass.UP:
                self.direction = newDirec
                self.turningPoints[self.head()] = self.direction
        else:
            #must be left
            if newDirec != SnakeClass.RIGHT:
                self.direction = newDirec
                self.turningPoints[self.head()] = self.direction

    def getPixels(self):
        """Returns a list of the pixels the snake is occupying. Pixels
        are represented by a list with 2 elements"""
        snakePixels = []
        for i in self.body:
            snakePixels.append(i[0])
        return snakePixels

    def getLength(self):
        """Returns the length of the snake"""
        return len(self.body)






















##        
