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
    class BodyPart :
        def __init__(self,coord,gameCanvas,playerSize,index):
            self.index = index
            self.gameCanvas = gameCanvas
            self.playerSize = playerSize
            #SPAWN PART
            (x,y,x2,y2) = coord
            self.obj = gameCanvas.create_rectangle(x,y,x2,y2)
            self.dirQueue = []
        def __del__(self):
            self.gameCanvas.delete(self.obj)

        def Enqueue(self,dir):
            #Ne pas dépasser la position de la partie dans la queue
            if(len(self.dirQueue) >= self.index):
                return
            self.dirQueue.append(dir)
        def Move(self,previousCoord):
            (dx,dy) = self.dirQueue.pop(0)
            (sx,sy) = self.playerSize
            (x1,y1,x2,y2) = previousCoord
            (gx,gy) = (dx*sx,sy*dy)
            self.gameCanvas.coords(self.obj,(x1-gx,y1-gy,x2-gx,y2-gy))
            return (dx,dy)


    def __init__(self,gameDimension,playerSize,foodSize,speed,refreshRate):
        #Assign Var
        self.foodSize = foodSize
        self.speed = speed
        self.dir = (0,0)
        self.playerSize = playerSize
        self.player = None
        self.parts = []
        self.refreshRate = refreshRate
        self.foodColor = 'red'

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
        self.parts =  []
        # Init Player
        (playerSizeX, playerSizeY) = self.playerSize
        self.player = self.gameCanvas.create_rectangle(self.width // 2, self.height // 2, self.width // 2 + playerSizeX,
                                                       self.height // 2 + playerSizeY)

        # Init Food
        self.food = self.Food(self, self.foodSize,self.foodColor)
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

        #Refresh Body Parts
        self.EnqueueBodyPartFrom((dx,dy))

        #Move body part
        #self.MoveBodyPart()

        #Try Eat Something
        self.TryEat((x1,y1,x2,y2))

        #CheckDeath
        if(self.CheckDeath()):
            self.ResetGame()

        self.gameCanvas.after(self.refreshRate,self.Move)
    def EnqueueBodyPartFrom(self, firstDir):
        firstCoord = self.gameCanvas.coords(self.player)
        dirs = [firstDir]
        for i in range(len(self.parts)):
            for dir in dirs:
                self.parts[i].Enqueue(dir)
            if(i==0):
                dirs.append( self.parts[i].Move(firstCoord))
            else:
                dirs.append(self.parts[i].Move(self.gameCanvas.coords(self.parts[i-1].obj)))
    def MoveBodyPart(self):
        for part in self.parts:
            part.Move()
    def TryEat(self,oldPos):
        (sx, sy) = self.playerSize
        if self.CheckDistanceBetweenTwoObj(self.player, self.food.obj,sx):
            self.food = self.Food(self,self.foodSize,self.foodColor)

            #ADD NEW BODY PART
            (x1, y1, x2, y2) = oldPos
            part = self.BodyPart((x1,y1,x2,y2),self.gameCanvas,self.playerSize,len(self.parts) +1)
            self.parts.append(part)
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
        for part in self.parts:
            (sx,sy)=self.playerSize
            if self.CheckDistanceBetweenTwoObj(self.player,part.obj,sx/2+0.001):
                return True
        return False

    #TOOL
    def getGap(self):
        (dx,dy) = self.dir
        (sx,sy) = self.playerSize
        return (dx*sx,dy*sy)


gameInstance = Game((500,300),(7,7),(7,7),6,50)

