class Cell:
    """
    Cette classe représente une cellule du jeu : Game of Life.
    """
    
    def __init__(self, life : bool) -> 'Cell':
        """
        Le constructeur d'une cellule.

        param : life - L'état de vie. True si elle est en vie, False sinon.
        """
        self.__life = life
        self.__neighbors = 0



    @property
    def life(self) -> bool:
        """
        Cette méthode renvoie l'état de vie de la cellule.

        return : Renvoie True si la cellule est vivante, False sinon.
        """
        return self.__life
    


    @life.setter
    def life(self, value : bool) -> None:
        """
        Cette méthode est interdite !

        raise : PermissionError - Si vous tentez de modifier l'attribut.
        """
        raise PermissionError("You don't have the acces to change this attribute.")
    


    def analyze(self, neighbors : list) -> None:
        """
        Cette méthode analyse le voisinage d'une cellule.

        param : Les voisines de la cellule, il doit en avoir exactement huit !
        """
        if len(neighbors) != 8:
            raise ValueError("The cell needs eight neighbors.")

        self.__neighbors = 0

        for cell in neighbors:
            if not isinstance(cell, Cell):
                raise ValueError("One of the cells is not a cell.")
            
            if cell.__life == True:
                self.__neighbors += 1
            else:
                cell.__neighbors += 1



    def update(self) -> None:
        """
        Cette méthode met à jour la cellule.
        """
        if self.__neighbors != 2 and self.__neighbors != 3:
            self.__life = False
        elif self.__neighbors == 3:
            self.__life = True






def addCell(cellsAlive : dict, x : int, y : int) -> None:
    """
    Cette fonction ajoute une cellule vivante dans cellsAlive.

    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : x - La composante X de la cellule.
    param : y - La composante Y de la cellule.
    """
    cellsAlive[(x, y)] = Cell(True)



def removeCell(cellsAlive : dict, x : int, y : int) -> None:
    """
    Cette fonction ajoute une cellule vivante dans cellsAlive.

    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : x - La composante X de la cellule.
    param : y - La composante Y de la cellule.
    """
    del cellsAlive[(x, y)]



def analyze(cellsAlive : dict) -> None:
    """
    Cette fonction analyse toutes les cellules.

    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    """
    cellsAliveCopy = cellsAlive.copy()
    for cellCoord in cellsAliveCopy:

        neighbors = []

        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):

                if x == 0 and y == 0:
                    continue

                coordX = x + cellCoord[0]
                coordY = y + cellCoord[1]

                if not (coordX, coordY) in cellsAlive:
                    cellsAlive[(coordX, coordY)] = Cell(False)

                neighbors.append(cellsAlive[(coordX, coordY)])

        cellsAlive[cellCoord].analyze(neighbors)



def update(cellsAlive : dict) -> None:
    """
    Cette fonction met à jour toutes les cellules.

    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    """
    cellsAliveCopy = cellsAlive.copy()
    for cellCoord in cellsAliveCopy:
        cellsAlive[cellCoord].update()
        
        if cellsAlive[cellCoord].life == False:
            removeCell(cellsAlive, cellCoord[0], cellCoord[1])
