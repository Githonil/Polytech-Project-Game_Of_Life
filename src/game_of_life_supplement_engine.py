import game_of_life_engine

class Cell(game_of_life_engine.Cell):
    """
    Cette classe représente une cellule du jeu : Game of Life.

    Ajout:
    -Les cellules ont des couleurs.
    """
    
    def __init__(self, life : bool, color : str) -> None:
        """
        Le constructeur d'une cellule.

        param : life - L'état de vie. True si elle est en vie, False sinon.
        param : color - Le nom de la couleur en anglais, ou en hexadécimal ex: #ff00ff.
        """
        game_of_life_engine.Cell.__init__(self, life)
        self.__color = color



    @property
    def color(self) -> None:
        """
        Cette méthode renvoie la couleur de la cellule.

        return : Renvoie la couleur de la cellule.
        """
        return self.__color
    


    @color.setter
    def color(self, value : str) -> None:
        """
        Cette méthode est interdite !

        raise : PermissionError - Si vous tentez d'accéder l'attribut.
        """
        raise PermissionError("You don't have the access to change this attribute.")
    





def addCell(cellsAlive : dict, x : int, y : int) -> None:
    """
    Cette fonction ajoute une cellule vivante dans cellsAlive.

    param : cellsAlive contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : x - La composante X de la cellule.
    param : y - La composante Y de la cellule.
    """
    game_of_life_engine.addCell(cellsAlive, x, y)



def removeCell(cellsAlive : dict, x : int, y : int) -> None:
    """
    Cette fonction ajoute une cellule vivante dans cellsAlive.

    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : x - La composante X de la cellule.
    param : y - La composante Y de la cellule.
    """
    game_of_life_engine.removeCell(cellsAlive, x, y)



def analyze(cellsAlive : dict, rows : int, columns : int) -> None:
    """
    Cette fonction analyse toutes les cellules.

    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : rows - Le nombre de lignes de la grille.
    param : columns - Le nombre de colonnes de la grille.
    """
    #TODO: Voir l'implémentation des naissances.
    game_of_life_engine.analyze(cellsAlive, rows, columns)



def update(cellsAlive : dict) -> None:
    """
    Cette fonction met à jour toutes les cellules.

    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    """
    game_of_life_engine.update(cellsAlive)
