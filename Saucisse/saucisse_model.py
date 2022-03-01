class Game:
    def __init__(self,gridSize):
        (sx,sy) = gridSize
        self.gridObj = Grid(sx,sy)

    
    
    #INTERACTION 
    def TrySubmitSaucisse(self,coord1,coord2,coord3):
        '''Essaye de créer une saucisse avec le set de 3 coordonnées, Retourne True si succès, retourne False sinon'''
        if(self.gridObj.IsReachable(coord1,coord2) and self.gridObj.IsReachable(coord2,coord3)):
            #SET SAUCISSE
            return True
        return False



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
                C.append(Point(i,j))
            self.grid.append(C)     
    def __str__(self):
        string = "["
        for column in self.grid:
            for point in column:
                if(point.isOccupied):
                    string += " X ,"
                else:
                    string += " O ,"
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
    
    def IsReachable(self,coord1,coord2):
        '''Retourne True si les deux points sont acceptés False sinon'''
        pass



    #METHOD DE TEST
    def MarkPointAt(self,x,y):
        self.grid[x][y].SetOccupied(True)
        
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.isOccupied = False
    def SetOccupied(self,isOccupied):
        self.isOccupied = isOccupied

grid = Grid()
grid.GetPointAt()
print(grid)