from tkinter import *

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
plateau = Canvas(game, width=300, height=200)
plateau.pack()
label1.pack()
label2.pack()


# Question 2.4
def move(canvas, id, dx, dy):
    (x1, y1, x2, y2) = canvas.coords(id)
    (x3, y3, x4, y4) = (x1 + dx, y1 + dy, x2 + dx, y2 + dy)
    if x4 > 300 or y4 > 200 or x3 < 0 or y3 < 0:
        return
    canvas.coords(id, (x3, y3, x4, y4))


<<<<<<< Updated upstream
#Quatre button de deplacement
buttonR = Button(menu,text="Move Right",command=lambda : move(plateau,pawn,10,0))
buttonL = Button(menu,text="Move Left",command=lambda :  move(plateau,pawn,-10,0))
buttonU = Button(menu,text="Move Up",command=lambda : move(plateau,pawn,0,10))
buttonD = Button(menu,text="Move Down",command=lambda : move(plateau,pawn,0,-10))
buttonChangeColor = Button(menu,text="Change Color",command=lambda :changeColor(pawn))
=======
# Pion
pawn = plateau.create_oval(150, 100, 175, 125)

# Quatre button de deplacement
buttonR = Button(menu, text="Move Right", command=lambda: move(plateau, pawn, 10, 0))
buttonL = Button(menu, text="Move Left", command=lambda: move(plateau, pawn, -10, 0))
buttonU = Button(menu, text="Move Up", command=lambda: move(plateau, pawn, 0, 10))
buttonD = Button(menu, text="Move Down", command=lambda: move(plateau, pawn, 0, -10))
>>>>>>> Stashed changes

buttonL.pack()
buttonD.pack()
buttonR.pack()
buttonU.pack()
buttonChangeColor.pack()

<<<<<<< Updated upstream
def changeToGreen(id):
    plateau.itemconfig(id,fill = "green")

def changeColor(id):
    attribute = plateau.itemconfig(id)
    (a,r,g,b,c) = attribute["fill"]
    c = "green" if c=="red" else "red"
    plateau.itemconfig(id,fill =c);


#Question 3.1
=======

def changeToGreen():
    plateau.itemconfig(id, fill="green")


# Question 3.1
>>>>>>> Stashed changes
def keyIn(evt):
    print("Vous avez appuyé sur la touche ", evt.char)


myWindow.bind("<Key>", keyIn)



myWindow.mainloop()

# emit from jetbrain
