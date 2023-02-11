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
    


    @property
    def neighbors(self) -> None:
        """
        Cette méthode est interdite !

        raise : PermissionError - Si vous tentez d'accéder l'attribut.
        """
        raise PermissionError("You don't have the acces to change this attribute.")
    


    @neighbors.setter
    def neighbors(self, value : int) -> None:
        """
        Cette méthode est interdite !

        raise : PermissionError - Si vous tentez d'accéder l'attribut.
        """
        raise PermissionError("You don't have the access to change this attribute.")
    


    def analyze(self, neighbors : list) -> None:
        """
        Cette méthode analyse le voisinage d'une cellule.

        param : Les voisines de la cellule, il doit en avoir exactement huit !
        """
        if len(neighbors) != 8:
            raise ValueError("The cell needs eight neighbors.")

        for cell in neighbors:
            if type(cell) != Cell:
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

    param : cellsAlive contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : x - La composante X de la cellule.
    param : y - La composante Y de la cellule.
    """
    cellsAlive[(x, y)] = Cell(True)



def removeCell(cellsAlive : dict, x : int, y : int) -> None:
    """
    Cette fonction ajoute une cellule vivante dans cellsAlive.

    param : cellsAlive contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : x - La composante X de la cellule.
    param : y - La composante Y de la cellule.
    """
    del cellsAlive[(x, y)]



def adjustBorder(coord : int, length : int) -> int:
    """
    Cette fonction ajuste une coordonnée selon une taille maximale.
    Si la coordonnée dépasse la taille, alors elle revient à 0.
    Si la coordonnée est en dessous de 0, alors elle revient à la taille maximale.
    
    param : coord - La coordonnée.
    param : length - La taille maximale.
    return : Renvoie la taille ajusté.
    """
    if coord > length:
        coord = 0
    elif coord < 0:
        coord = length
        
    return coord



def analyze(cellsAlive : dict, rows : int, columns : int) -> None:
    """
    Cette fonction analyse toutes les cellules.

    param : cellsAlive contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : rows - Le nombre de lignes de la grille.
    param : columns - Le nombre de colonnes de la grille.
    """
    for cellCoord in cellsAlive:

        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):

                coordX = x + cellCoord[0]
                coordY = y + cellCoord[1]

                coordX = adjustBorder(coordX, columns)
                coordY = adjustBorder(coordY, rows)

                if not (coordX, coordY) in cellsAlive:
                    cellsAlive[(coordX, coordY)] = Cell(False)

                cellsAlive[cellCoord].analyze()



def update(cellsAlive : dict) -> None:
    """
    Cette fonction met à jour toutes les cellules.

    param : cellsAlive contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    """
    for cellCoord in cellsAlive:
        cellsAlive[cellCoord].update()
        
        if cellsAlive[cellCoord].life == False:
            removeCell(cellsAlive, cellCoord[0], cellCoord[1])