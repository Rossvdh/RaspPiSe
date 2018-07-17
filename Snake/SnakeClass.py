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
        self.body = [[[4,1], DOWN], [[4,0], DOWN]]

        self.turningPoints = {}
        self.direction  = DOWN

    def head(self):
        """Returns a tuple with co-ords of the head of the snake"""
        return tuple(body[0][0])

    def slither(self, food, alive):
        """Moves the snake and food's co-ordinates, but does not set the LEDs
        in the matrix."""
        newSegment = []

        for i in range(len(snake)):
            segment = snake[i]
            #convert to tuple because a list can't be used as a
            #dictionary key
            pixel = tuple(segment[0])

            # check for turning point
            if pixel in turningPoints.keys():
                segment[1] = turningPoints[pixel]
                
                #if all points in the snake have passed, remove the TP
                if i == len(snake)-1:
                    #being removed before the newly added segment gets to it
                    turningPoints.pop(pixel)

            if i == 0 and pixel == tuple(food):
                # the head eats the food
                # snake grows (new segment to be added)
                newSegment = list(snake[len(snake)-1])
                newSegment[0] = list(newSegment[0])
                snake.append(newSegment)
                
                #move food
                food = generateFood()

            #move the snake
            dire = segment[1]
            if dire == UP:
                segment[0][1] -=1
            elif dire == LEFT:
                segment[0][0] -=1
            elif dire == DOWN:
                segment[0][1] +=1
            else:
                segment[0][0] +=1

            #check if new position is in the snake
            snakePixels = []
            for i in snake:
                snakePixels.append(i[0])

            if snakePixels.count(segment[0]) > 1:
                die()
                return

    def changeDirection(self, newDirec):
        """Changes the direction of the Snake's movement"""
        if self.direction == UP:
            if newDirec != DOWN:
                self.direction = newDirec
                self.turningPoints[head()] = self.direction
        elif self.direction == RIGHT:
            if newDirec != LEFT:
                self.direction = newDirec
                self.turningPoints[head()] = self.direction
        elif self.direction == DOWN:
            if newDirec != UP:
                self.direction = newDirec
                self.turningPoints[head()] = self.direction
        else:
            #must be left
            if newDirec != RIGHT:
                self.direction = newDirec
                self.turningPoints[head()] = self.direction

    def getPixels(self):
        """Returns a list of the pixels the snake is occupying. Pixels
        are represented by a list with 2 elements"""
        snakePixels = []
        for i in snake:
            snakePixels.append(i[0])
        return snakePixels
























##        
