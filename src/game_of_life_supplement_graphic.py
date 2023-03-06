import game_of_life_graphic

import tkinter

class GameOfLifeGraphic(game_of_life_graphic.GameOfLifeGraphic):
    """
    Cette classe représente l'interface graphique du jeu : Game of Life.
    Ajout:
    -Choix des couleurs.
    """

    def __init__(self, width : int, height : int, columns : int, rows : int) -> 'GameOfLifeGraphic':
        """
        Le constructeur de l'interface graphique.

        param : width - La largeur de la zone de dessin.
        param : height - La hauteur de la zone de dessin.
        param : columns - Le nombre de colonnes dans la grille.
        param : rows - Le nombre de lignes dans la grille.
        """
        super().__init__(width, height, columns, rows)
        self.__colorsSet = set()
        self.countCellsRed = tkinter.IntVar() #Cet attribut représente le nombres des cellules rouges en vie.
        self.countCellsGreen = tkinter.IntVar() #Cet attribut représente le nombres des cellules verts en vie.
        self.countCellsBlue = tkinter.IntVar() #Cet attribut représente le nombres des cellules bleues en vie.



    def __updateColor(self, color : str) -> None:
        """
        Cette méthode met à jour une couleur.
        Si la couleur est activé alors elle se désactive.
        Si la couleur est désactivé alors elle s'active.

        param : color - La couleur à mettre à jour.
        """
        if color in self.__colorsSet:
            self.__colorsSet.remove(color)
        else:
            self.__colorsSet.add(color)



    def _initColor(self) -> None:
        """
        Cette méthode initialise les boutons de couleur
        """
        redButton = tkinter.Checkbutton(self._menuFrame, bg="red", width=3, command=lambda : self.__updateColor("red"))
        greenButton = tkinter.Checkbutton(self._menuFrame, bg="green", width=3, command=lambda : self.__updateColor("green"))
        blueButton = tkinter.Checkbutton(self._menuFrame, bg="blue", width=3, command=lambda : self.__updateColor("blue"))
        redButton.grid(row=self._rowIndex, column=self._columnIndex, columnspan=3, padx=10, pady=10)
        self._columnIndex += 1
        greenButton.grid(row=self._rowIndex, column=self._columnIndex, columnspan=3, padx=10, pady=10)
        self._columnIndex += 1
        blueButton.grid(row=self._rowIndex, column=self._columnIndex, columnspan=3, padx=10, pady=10)
        self._columnIndex = 0
        self._rowIndex += 1



    @property
    def colorsSet(self) -> set:
        """
        Cette méthode renvoie le set des couleurs active.

        return : Renvoie le set des couleurs active.
        """
        return self.__colorsSet
    


    @colorsSet.setter
    def colorsSet(self, value : set) -> None:
        """
        Cette méthode est interdite !
        raise : PermissionError - Si vous tentez de modifier l'attribut.
        """
        raise PermissionError("You don't have the acces to change this attribute.")
    


    def _countCells(self) -> None:
        """
        Cette méthode ajoute le conteur de cellules en vie.
        """
        label = tkinter.Label(self._menuFrame, text="cells red alive : ", font=self.__font, bg="black", fg="white")
        label.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)
        self._columnIndex += 1

        label = tkinter.Label(self._menuFrame, textvariable=self.countCellsRed, font=self.__font, bg="black", fg="white")
        label.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)

        self._columnIndex = 0
        self._rowIndex += 1

        label = tkinter.Label(self._menuFrame, text="cells green alive : ", font=self.__font, bg="black", fg="white")
        label.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)
        self._columnIndex += 1

        label = tkinter.Label(self._menuFrame, textvariable=self.countCellsGreen, font=self.__font, bg="black", fg="white")
        label.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)

        self._columnIndex = 0
        self._rowIndex += 1

        label = tkinter.Label(self._menuFrame, text="cells blue alive : ", font=self.__font, bg="black", fg="white")
        label.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)
        self._columnIndex += 1

        label = tkinter.Label(self._menuFrame, textvariable=self.countCellsBlue, font=self.__font, bg="black", fg="white")
        label.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)

        self._columnIndex = 0
        self._rowIndex += 1
    


    def _text(self) -> None:
        """
        Cette méthode ajoute le texte explicatif.
        """
        label = tkinter.Label(text="""Hello and welcome to the game of life.
The rules are simple.
On a grid of cells,
cells will evolve with these rules:

-A cell alone dies.
-A cell with more than 3 neighbors die.
-A cell with exactly 3 neighbors birth.

To add a cell, chose one or many colors
and right click in the grid
(to remove continue to right click
until the cell is erased).
You can adjust the time with
the Ticks per seconds scrollbar.

Good game !""", font="Times_New_Roman 12", bg="black", fg="white"
        )
        label.grid(row=0, column=0)



    def init(self) -> None:
        """
        Cette méthode initialise l'interface.
        """
        self._initRoot()
        self._text()
        self._initCanvas()
        self._initMenu()
        self._initTimeRange()
        self._initColor()
        self._initRandom()
        self._initStartButton()
        self._initSaveButton()
        self._initEvent()
        self._countCells()



    def render(self, coords : dict) -> None:
        """
        Cette méthode fait le rendu de l'interface graphique.

        param : coords - La map où se trouve les cellules et leur couleur (clef : (coordX, coordY), value : color:str).
        """
        for coord in coords.keys():
            coordX = coord[0] * self.__cellWidth
            coordY = coord[1] * self.__cellHeight

            if not coord in self.__sprites:
                self.__sprites[coord] = self.__canvas.create_rectangle(coordX, coordY, coordX + self.__cellWidth - 1, coordY + self.__cellHeight - 1, fill=coords[coord], outline="")
            else:
                self.__canvas.itemconfig(self.__sprites[coord], fill=coords[coord])

        spritesCopy = self.__sprites.copy()
        for sprite in spritesCopy:

            if not sprite in coords.keys():
                self.__canvas.delete(self.__root, self.__sprites[sprite])
                del self.__sprites[sprite]

        self.__canvas.update()
            