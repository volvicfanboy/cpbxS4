import random
from tkinter import *
from math import *

#GLOBAL VAR
threahold = 15
pawnRadius = 30
(screenWidth, screenHeight) = (300, 200)
food=None


myWindow = Tk()
# L=Label(myWindow,text = "blabla")
# L.pack()
# B=Button(myWindow,text = "Quitter",command = myWindow.destroy)
# B.pack()
# myWindow.mainloop()

# Le label est un widget pour afficher du texte. Le button permet d'executer une method.


# Question 2.1
menu = Frame(myWindow)
game = Frame(myWindow)
menu.pack(side=LEFT)
game.pack(side=RIGHT)
label1 = Label(menu, text="Menu de configuration")
label2 = Label(game, text="Plateau de jeu")
plateau = Canvas(game, width=screenWidth, height=screenHeight)
plateau.pack()
label1.pack()
label2.pack()


# Question 4.1
class foodObj():
    def __init__(self,canvas):
        self.obj =None
        self.score = IntVar()
        self.spawnNewFood(canvas)

    def newFoodPos(self):
        return random.randint(0, screenWidth-10), random.randint(0, screenHeight-10)

    def spawnNewFood(self, canvas):
        self.score.set(self.score.get() + 1)
        canvas.delete(self.obj)
        self.coord = self.newFoodPos()
        (x, y) = self.coord
        self.obj = canvas.create_oval(x, y, x + 10, y + 10)
    def checkPawn(self,plateau, pawn):
        (x, y, x2, y2) = plateau.coords(pawn)
        (xf, yf) = self.coord
        print(food.coord)
        print(((x + x2) / 2),((y + y2) / 2))
        if abs(((x + x2) / 2) - xf) < threahold and abs(((y + y2) / 2) - yf) < threahold:
            self.spawnNewFood(plateau)
            changeColor(pawn)


#Question 4.1 fin

# Question 2.4
def move(canvas, id, dx, dy, _foodDp):
    (x1, y1, x2, y2) = canvas.coords(id)
    (x3, y3, x4, y4) = (x1 + dx, y1 + dy, x2 + dx, y2 + dy)
    if x4 > screenWidth or y4 > screenHeight or x3 < 0 or y3 < 0:
        return
    canvas.coords(id, (x3, y3, x4, y4))
    _foodDp.checkPawn(canvas, id)


# Pion qui spawn aléatoirement sur le plateau
(pawnX,pawnY) = (random.randint(0,screenWidth),random.randint(0,screenHeight))
pawn = plateau.create_oval(pawnX, pawnY, pawnX+pawnRadius, pawnY+pawnRadius)


# Quatre button de déplacement
buttonR = Button(menu, text="Move Right", command=lambda : move(plateau, pawn, 10, 0, food))
buttonL = Button(menu, text="Move Left", command=lambda: move(plateau, pawn, -10, 0, food))
buttonU = Button(menu, text="Move Up", command=lambda: move(plateau, pawn, 0, 10, food))
buttonD = Button(menu, text="Move Down", command=lambda: move(plateau, pawn, 0, -10, food))
buttonChangeColor = Button(menu, text="Change Color", command=lambda: changeColor(pawn))


buttonL.pack()
buttonD.pack()
buttonR.pack()
buttonU.pack()
buttonChangeColor.pack()


def changeToGreen(id):
    plateau.itemconfig(id, fill="green")
def changeColor(id):
    attribute = plateau.itemconfig(id)
    (a, r, g, b, c) = attribute["fill"]
    c = "green" if c == "red" else "red"
    plateau.itemconfig(id, fill=c);


# Question 3.1
def keyIn(evt):
    print("Vous avez appuyé sur la touche ", evt.char)
myWindow.bind("<Key>", keyIn)

# Question 3.3
def foo(evt):
    if(evt.char == 'z'):
        move(plateau,pawn,0,-10,food)
    if(evt.char == 'q'):
        move(plateau,pawn,-10,0,food)
    if(evt.char == 's'):
        move(plateau,pawn,0,10,food)
    if(evt.char == 'd'):
        move(plateau,pawn,10,0,food)

myWindow.bind("<Key>", foo)


# Question 4.1



food = foodObj(plateau)

scoreDp = Label(menu, textvariable=food.score)
scoreDp.pack()



myWindow.mainloop()

