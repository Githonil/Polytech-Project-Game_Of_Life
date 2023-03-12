import tkinter
from tkinter import filedialog
import pickle

class GameOfLifeGraphic:
    """
    Cette classe représente l'interface graphique du jeu : Game of Life.
    """

    def __init__(self, width : int, height : int, columns : int, rows : int) -> 'GameOfLifeGraphic':
        """
        Le constructeur de l'interface graphique.
        param : width - La largeur de la zone de dessin.
        param : height - La hauteur de la zone de dessin.
        param : columns - Le nombre de colonnes dans la grille.
        param : rows - Le nombre de lignes dans la grille.
        """
        self.__width = width
        self.__height = height
        self.__columns = columns
        self.__rows = rows
        self.__cellWidth = self.__width // self.__columns
        self.__cellHeight = self.__height // self.__rows
        self.__root = tkinter.Tk()
        self.__canvas = tkinter.Canvas(self.__root)
        self._menuFrame = tkinter.Frame(self.__root)
        self.__randomButton = tkinter.Button(self._menuFrame)
        self.__startButton = tkinter.Button(self._menuFrame)
        self.__stopButton = tkinter.Button(self._menuFrame)
        self.__resetButton = tkinter.Button(self._menuFrame)
        self.__saveButton = tkinter.Button(self._menuFrame)
        self.__importButton = tkinter.Button(self._menuFrame)
        self.__tpsRange = tkinter.IntVar()
        self.__randomRange = tkinter.IntVar()
        self._rowIndex = 0
        self._columnIndex = 0
        self.__font = "Times_New_Roman 12"
        self.__sprites = {}
        self.__mouseX = -1
        self.__mouseY = -1
        self.eventDetect = False #Cet attribut permet de dire si un évènement à eu lieu. à remettre à False si jamais.
        self.motionDetect = False #Cet attribut permet de dire si un évènement à mouvement à eu lieu. à remettre à False si jamais.
        self.countCells = tkinter.IntVar() #Cet attribut représente le nombre de cellules en vie.



    def _initRoot(self) -> None:
        """
        Cette méthode initialise la racine de l'interface.
        """
        self.__root.title("Game of Life")
        self.__root.config(bg="black")
        self.__root.resizable(width=False, height=False)



    def _initCanvas(self) -> None:
        """
        Cette méthode initialise le canvas de l'interface
        """
        self.__canvas.config(width=self.__width, height=self.__height, bg="white", highlightthickness=0)
        self.__canvas.grid(row=0, column=1)

        self.__initRender()



    def __initRender(self) -> None:
        """
        Cette méthode initialise le rendu.
        """
        for x in range(self.__cellWidth, self.__width + 1, self.__cellWidth):
            self.__canvas.create_rectangle(x - 1, 0, x - 1, self.__height, fill="black", outline="")

        for y in range(self.__cellHeight, self.__height + 1, self.__cellHeight):
            self.__canvas.create_rectangle(0, y - 1, self.__width, y - 1, fill="black", outline="")



    def _initMenu(self) -> None:
        """
        Cette méthode initialise le menu de l'interface.
        """
        self._menuFrame.config(bg="black")
        self._menuFrame.grid(row=0, column=2)

        label = tkinter.Label(self._menuFrame, text="Game of Life", font="Courier 22 bold", fg="white", bg="black")
        label.grid(row=self._rowIndex, column=0, columnspan=100, padx=10, pady=10)
        self._rowIndex += 1



    def _initTimeRange(self) -> None:
        """
        Cette méthode initialise le range du TPS.
        """
        textFR = "Actions par seconde"
        textEN = "Ticks per second"
        label = tkinter.Label(self._menuFrame, text=textFR, font=self.__font, fg="white", bg="black")
        label.grid(row=self._rowIndex, column=self._columnIndex, columnspan=100, padx=10, pady=10)
        self._rowIndex += 1

        range = tkinter.Scale(self._menuFrame, from_=0.01, to_=2.0, resolution=0.01, variable=self.__tpsRange, orient=tkinter.HORIZONTAL)
        range.grid(row=self._rowIndex, column=self._columnIndex, columnspan=100, padx=10, pady=10)
        self._rowIndex += 1



    def getTimeRange(self) -> float:
        """
        Cette méthode renvoie le TPS.
        param : Renvoie le TPS.
        """
        return self.__tpsRange.get()



    def _initRandom(self) -> None:
        """
        Cette méthode initialise les bouttons de random.
        """
        textFR = "Random (en %)"
        textEN = "Random (in %)"
        label = tkinter.Label(self._menuFrame, text=textFR, font=self.__font, fg="white", bg="black")
        label.grid(row=self._rowIndex, column=self._columnIndex, columnspan=100, padx=10, pady=10)
        self._rowIndex += 1

        self.__randomButton.config(text="Random", font=self.__font)
        self.__randomButton.grid(row=self._rowIndex, column=self._columnIndex, columnspan=3, padx=10, pady=10)
        self._columnIndex += 2

        range = tkinter.Scale(self._menuFrame, from_=25, to_=100, resolution=1, variable=self.__randomRange, orient=tkinter.HORIZONTAL)
        range.grid(row=self._rowIndex, column=self._columnIndex, columnspan=4, padx=10, pady=10)
        self._columnIndex = 0
        self._rowIndex += 1



    def getRandomRange(self) -> int:
        """
        Cette méthode renvoie la valeur du random range.
        return : Renvoie la valeur du random range.
        """
        return self.__randomRange.get()



    def setRandomButton(self, func: 'function') -> None:
        """
        Cette méthode modifie la fonction du bouton random.
        param : func - La nouvelle fonction.
        """
        self.__randomButton.config(command=func)



    def _initStartButton(self) -> None:
        """
        Cette méthode initialise les boutons start, stop et reset.
        """
        self.__startButton.config(text="Start", font=self.__font)
        self.__startButton.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)
        self._columnIndex += 1

        self.__stopButton.config(text="Stop", font=self.__font)
        self.__stopButton.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)
        self._columnIndex += 1

        self.__resetButton.config(text="Reset", font=self.__font)
        self.__resetButton.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)
        self._columnIndex += 1



    def setStartButton(self, func : 'function') -> None:
        """
        Cette méthode modifie la fonction du bouton start.
        param : func - La nouvelle fonction.
        """
        self.__startButton.config(command=func)



    def setStopButton(self, func : 'function') -> None:
        """
        Cette méthode modifie la fonction du bouton stop.
        param : func - La nouvelle fonction.
        """
        self.__stopButton.config(command=func)



    def setResetButton(self, func : 'function') -> None:
        """
        Cette méthode modifie la fonction du bouton reset.
        param : func - La nouvelle fonction.
        """
        self.__resetButton.config(command=func)



    def _initSaveButton(self) -> None:
        """
        Cette méthode initialise les boutons start, stop et reset.
        param : row - La ligne où ça commence.
        param : column - La colonne où ça commence.
        """
        self.__saveButton.config(text="Save", font=self.__font)
        self.__saveButton.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)
        self._columnIndex += 1

        self.__importButton.config(text="Import", font=self.__font)
        self.__importButton.grid(row=self._rowIndex, column=self._columnIndex, padx=10, pady=10)
        
        self._columnIndex = 0
        self._rowIndex += 1



    def setSaveButton(self, func : 'function') -> None:
        """
        Cette méthode modifie la fonction du bouton save.
        param : func - La nouvelle fonction.
        """
        self.__saveButton.config(command=func)



    def setImportButton(self, func : 'function') -> None:
        """
        Cette méthode modifie la fonction du bouton import.
        param : func - La nouvelle fonction.
        """
        self.__importButton.config(command=func)



    def _countCells(self) -> None:
        """
        Cette méthode ajoute le conteur de cellules en vie.
        """
        textFR = "cellules en vie : "
        textEN = "cells alive : "
        label = tkinter.Label(self._menuFrame, text=textFR, font=self.__font, bg="black", fg="white")
        label.grid(row=self._rowIndex, column=self._columnIndex, columnspan=3, padx=10, pady=10)
        self._columnIndex += 3

        label = tkinter.Label(self._menuFrame, textvariable=self.countCells, font=self.__font, bg="black", fg="white")
        label.grid(row=self._rowIndex, column=self._columnIndex, columnspan=2, padx=10, pady=10)

        self._columnIndex = 0
        self._rowIndex += 1


    def _text(self) -> None:
        """
        Cette méthode ajoute le texte explicatif.
        """
        textFR = """Bonjour et bienvenue dans le jeu de la vie.
Les règles sont simples.
Sur une grille de case,
des cellules vont évoluer avec ces régles:
-Une cellule seule meurt.
-Une cellule avec plus de 3 voisines meurt.
-Une case avec exactement 3 voisines naît.
Pour ajouter une cellule, faire un clique droit sur la grille
(Un second click pour retirer).
Vous pouvez régler le temps avec
la barre Actions par seconde.
Bon jeu !"""

        textEN = """Hello and welcome to the game of life.
The rules are simple.
On a grid of cells,
cells will evolve with these rules:
-A cell alone dies.
-A cell with more than 3 neighbors dies.
-A cell with exactly 3 neighbors births.
To add a cell right click in the grid
(a second click to remove).
You can adjust the time with
the Ticks per seconds scrollbar.
Good game !"""

        label = tkinter.Label(text=textFR, font="Times_New_Roman 12", bg="black", fg="white"
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
        self._initRandom()
        self._initStartButton()
        self._initSaveButton()
        self._initEvent()
        self._countCells()



    def __binding(self, event : 'tkinter.Event') -> None:
        """
        Cette méthode agit sur le binding des évènements.
        param : Le registre des évènements.
        """
        self.__mouseX = (event.x - (event.x % self.__cellWidth))  // self.__cellWidth
        self.__mouseY = (event.y - (event.y % self.__cellHeight))  // self.__cellHeight
        self.eventDetect = True



    def __bindingMotion(self, event : 'tkinter.Event') -> None:
        """
        Cette méthode agit sur le binding des évènements en mouvement.
        param : Le registre des évènements.
        """
        self.motionDetect = True
        self.__binding(event)



    def _initEvent(self) -> None:
        """
        Cette méthode initialise les évènements.
        """
        self.__canvas.bind("<Button-1>", self.__binding)
        self.__canvas.bind("<B1-Motion>", self.__bindingMotion)



    def getMouseX(self) -> int:
        """
        Cette méthode renvoie l'indice de la colonne de la dernière case clicker.
        return : Renvoie l'indice de la colonne de la dernière case clicker.
        """
        old = self.__mouseX
        self.__mouseX = -1
        return old
    


    def getMouseY(self) -> int:
        """
        Cette méthode renvoie l'indice de la ligne de la dernière case clicker.
        return : Renvoie l'indice de la ligne de la dernière case clicker.
        """
        old = self.__mouseY
        self.__mouseY = -1
        return old
    


    def initQuitButton(self, func : 'function') -> None:
        """
        Cette méthode met à jour le bouton fermer de l'interface graphique.
        param : func - La fonction.
        """
        self.__root.protocol("WM_DELETE_WINDOW", func=func)



    def render(self, coords : list) -> None:
        """
        Cette méthode fait le rendu de l'interface graphique.
        param : coords - La liste des coordonnées d'une cellule. (coordX, coordY).
        """
        for coord in coords:
            coordX = coord[0] * self.__cellWidth
            coordY = coord[1] * self.__cellHeight

            if not coord in self.__sprites:
                self.__sprites[coord] = self.__canvas.create_rectangle(coordX, coordY, coordX + self.__cellWidth - 1, coordY + self.__cellHeight - 1, fill="black", outline="")

        spritesCopy = self.__sprites.copy()
        for sprite in spritesCopy:

            if not sprite in coords:
                self.__canvas.delete(self.__root, self.__sprites[sprite])
                del self.__sprites[sprite]

        self.__canvas.update()
            



    def lunch(self) -> None:
        """
        Cette fonction lance l'interface graphique.
        """
        self.__canvas.mainloop()



    @staticmethod
    def save(obj : object) -> None:
        """
        Cette méthode statique permet d'avoir une fenêtre de sauvegarde d'un objet.
        param : obj - L'objet à sauvegarder.
        """
        file = filedialog.asksaveasfile(initialdir="./", mode="wb", defaultextension=".py", filetypes=[("Save file", ".save")])

        if file == None:
            return

        pickle.dump(obj, file)
        file.close()



    @staticmethod
    def import_obj() -> object:
        """
        Cette méthode statique permet de charger un objet dans un fichier.
        return : Renvoie l'objet importer. Renvoie None, si l'action est annulée.
        """
        file = filedialog.askopenfile(initialdir="./", mode="rb", defaultextension=".py", filetypes=[("Save file", ".save")])

        if file == None:
            return

        obj = pickle.load(file)
        file.close()
        return obj