import random
from tkinter import *



#Question 1.1

class Game:

    class Food:
        def __init__(self,game,foodSize,foodColor):
            self.game = game
            self.foodSize = foodSize
            self.foodColor = foodColor

            #Init first food
            self.obj = None
            self.newRandCoord()
            self.spawnFood()
        def newRandCoord(self):
            self.coord = (random.randint(0,self.game.width),random.randint(0,self.game.height))
        def spawnFood(self):
            self.game.gameCanvas.delete(self.obj)
            (x,y) = self.coord
            (sx,sy)=self.foodSize
            self.obj = self.game.gameCanvas.create_rectangle(x,y,x+sx,y+sy)
            self.game.gameCanvas.itemconfig(self.obj,fill=self.foodColor)
        def __del__(self):
            self.game.gameCanvas.delete(self.obj)


    def __init__(self,gameDimension,playerSize,speed):
        #Assign Var
        self.speed = speed
        self.dir = (0,0)
        self.playerSize = playerSize
        self.player = None

        #Init game windows and canvas
        (tempX,tempY) = gameDimension
        self.width = tempX
        self.height = tempY
        self.gameWindows = Tk()
        self.gameCanvas = Canvas(self.gameWindows,width=self.width,height=self.height)
        self.gameCanvas.pack()

        #Init Game
        self.ResetGame()

        #Event
        self.gameWindows.after(300,self.Move)

        #Bind Key
        self.gameWindows.bind('<z>',self.ChangeDirection)
        self.gameWindows.bind('<s>',self.ChangeDirection)
        self.gameWindows.bind('<q>',self.ChangeDirection)
        self.gameWindows.bind('<d>',self.ChangeDirection)

        self.gameWindows.mainloop()

    def ResetGame(self):
        #Remove existant
        if(self.player != None):
            self.gameCanvas.delete(self.player)

        # Init Player
        (playerSizeX, playerSizeY) = self.playerSize
        self.player = self.gameCanvas.create_rectangle(self.width // 2, self.height // 2, self.width // 2 + playerSizeX,
                                                       self.height // 2 + playerSizeY)

        # Init Food
        self.food = self.Food(self, (3, 3), 'red')



    def ChangeDirection(self,evt):
        if(evt.char == 'z'):
            self.dir = (0,-1)
        if(evt.char == 's'):
            self.dir = (0,1)
        if(evt.char == 'q'):
            self.dir = (-1,0)
        if(evt.char == 'd'):
            self.dir = (1,0)
    def Move(self):
        (dx,dy) = self.dir
        (x1, y1, x2, y2) = self.gameCanvas.coords(self.player)
        (x3, y3, x4, y4) = (x1 + self.speed * dx, y1 + self.speed * dy,x2 + self.speed * dx, y2 + self.speed * dy)
        self.gameCanvas.coords(self.player, (x3, y3, x4, y4))
        self.gameCanvas.after(1,self.Move)

        #Try Eat Something
        self.TryEat()

        #CheckDeath
        if(self.CheckDeath()):
            self.ResetGame()
    def TryEat(self):
        if self.CheckDistanceBetweenTwoObj(self.player, self.food.obj, 2):
            self.food.newRandCoord()
            self.food.spawnFood()
        pass
    def CheckDistanceBetweenTwoObj(self,id1,id2,threahold):
        (x, y, x2, y2) = self.gameCanvas.coords(id1)
        (xp1,yp1,xp2,yp2) = self.gameCanvas.coords(id2)
        if abs(((x + x2) / 2) - ((xp1 + xp2) / 2)) < threahold and abs(((y + y2) / 2) - ((yp1 + yp2) / 2)) < threahold:
            return True
        return False
    def CheckDeath(self):
        (x1,y1,x2,y2) = self.gameCanvas.coords(self.player)
        (x,y) = ((x1+x2)//2,(y1+y2)//2)
        if(x > self.width or x<0):
            return True
        if(y > self.height or y<0):
            return True
        return False





gameInstance = Game((500,300),(2,2),0.4)