class Game:
    def __init__(self,gridSize):
        (sx,sy) = gridSize
        self.gridObj = Grid(sx,sy)

        self.p1Saucisses = []
        self.p2Saucisses = []

        self.isP1Turn = True;

    
    
    #INTERACTION 
    def TrySubmitSaucisse(self,coord1,coord2,coord3):
        '''Essaye de créer une saucisse avec le set de 3 coordonnées, Retourne True si succès, retourne False sinon'''
        if(self.gridObj.IsReachable(coord1,coord2) and self.gridObj.IsReachable(coord2,coord3)):
            #SET SAUCISSE
            self.__SetSaucisse(coord1,coord2,coord3)
            return True
        return False
    def __SetSaucisse(self,coord1,coord2,coord3):
        point1 = self.gridObj.GetPointAt(coord1)
        point2 = self.gridObj.GetPointAt(coord2)
        point3 = self.gridObj.GetPointAt(coord3)

        if(self.isP1Turn):
            self.p1Saucisses.append((point1,point2,point3))
        else:
            self.p2Saucisses.append((point1,point2,point3))





class Grid:
    '''
    Class représentant la grille de jeu.
    '''
    def __init__(self,width=8,height=5):
        #ASSIGNATION DES ATTRIBUTS
        self.grid = []
        self.width = width
        self.height = height

        #CREATION DE LA GRILLE 
        for i in range(height):
            C = []
            for j in range(width):
                C.append(Point(i,j,(i+j)%2 != 0))
            self.grid.append(C)     
    def __str__(self):
        string = "["
        for column in self.grid:
            for point in column:
                if(point.isOccupied and not(point.isFictif)):
                    string += " X ,"
                elif(not(point.isOccupied) and not(point.isFictif)):
                    string += " O ,"
                else:
                    string += "- ,"
            string += '\n'
        string += "]"
        return string
    #GETTER / SETTER
    def GetPointAt(self,x,y):
        '''Retourne le point au coordonnée (x,y), None si les coordonnées ne sont pas dans grille.'''
        if(x<0 or y<0 or x>=self.width or y>=self.height):
            return None
        else:
            return self.grid[x][y]
    #Overloaded method to be compatible with tuples.
    def GetPointAt(self,coord):
        '''Retourne le point au coordonnée (x,y), None si les coordonnées ne sont pas dans grille'''
        (x,y) = coord;
        if (x < 0 or y < 0 or x >= self.width or y >= self.height):
            return None
        else:
            return self.grid[x][y]
    
    def IsReachable(self,coord1,coord2):
        '''Retourne True si les deux points sont acceptés False sinon'''
        #CHECK POINT ARE NOT EQUAL
        (x1,y1) = coord1
        (x2,y2) = coord2

        point1 = self.grid[x1][y1]
        point2 = self.grid[x2][y2]

        if(x1 == x2 and y1 == y2):
            return False
        #CHECK POINT ARE NOT OCCUPIED
        if(point1.isOccupied or point2.isOccupied):
            return False
        #CALCUL DX AND DY
        dx = x2-x1
        dy = y2-y1
        #CHECK DISTANCE
        if(dx + dy > 2):
            return False
        if(dx == 2 and self.grid[x1+1][y1].isOccupied):
            return False
        if(dy == 2 and self.grid[x1][y1+1].isOccupied):
            return False
        return True


        pass



    #METHOD DE TEST
    def MarkPointAt(self,x,y):
        self.grid[x][y].SetOccupied(True)
        
class Point:
    def __init__(self,x,y,isFictif=False):
        self.x = x
        self.y = y
        self.isOccupied = False
        self.isFictif = isFictif
    def SetOccupied(self,isOccupied):
        self.isOccupied = isOccupied

grid = Grid()
grid.MarkPointAt(2,2)
print(grid)