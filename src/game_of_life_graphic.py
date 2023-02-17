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
        self.__menuFrame = tkinter.Frame(self.__root)
        self.__randomButton = tkinter.Button(self.__menuFrame)
        self.__startButton = tkinter.Button(self.__menuFrame)
        self.__stopButton = tkinter.Button(self.__menuFrame)
        self.__resetButton = tkinter.Button(self.__menuFrame)
        self.__saveButton = tkinter.Button(self.__menuFrame)
        self.__importButton = tkinter.Button(self.__menuFrame)
        self.__tpsRange = tkinter.IntVar()
        self.__randomRange = tkinter.IntVar()
        self.__rowIndex = 0
        self.__columnIndex = 0



    def __initRoot(self) -> None:
        """
        Cette méthode initialise la racine de l'interface.
        """
        self.__root.title("Game of Life")
        self.__root.config(bg="black")
        self.__root.resizable(width=False, height=False)



    def __initCanvas(self) -> None:
        """
        Cette méthode initialise le canvas de l'interface
        """
        self.__canvas.config(width=self.__width, height=self.__height, bg="white", highlightthickness=0)
        self.__canvas.grid(row=0, column=0)



    def __initRender(self) -> None:
        """
        Cette méthode initialise le rendu.
        """
        for x in range(self.__cellWidth, self.__width, self.__cellWidth):
            self.__canvas.create_rectangle(x, 0, x, self.__height, fill="black", outline="")

        for y in range(self.__cellHeight, self.__height, self.__cellHeight):
            self.__canvas.create_rectangle(0, y, self.__width, y, fill="black", outline="")



    def __initMenu(self) -> None:
        """
        Cette méthode initialise le menu de l'interface.
        """
        self.__menuFrame.config(bg="black")
        self.__menuFrame.grid(row=0, column=1)

        label = tkinter.Label(self.__menuFrame, text="Game of Life", font="Courier 22 bold", fg="white", bg="black")
        label.grid(row=self.__rowIndex, column=0, columnspan=100, padx=10, pady=10)
        self.__rowIndex += 1



    def __initTimeRange(self) -> None:
        """
        Cette méthode initialise le range du TPS.
        """
        label = tkinter.Label(self.__menuFrame, text="Ticks per second", font="Courier 12", fg="white", bg="black")
        label.grid(row=self.__rowIndex, column=self.__columnIndex, columnspan=100, padx=10, pady=10)
        self.__rowIndex += 1

        range = tkinter.Scale(self.__menuFrame, variable=self.__tpsRange, orient=tkinter.HORIZONTAL)
        range.grid(row=self.__rowIndex, column=self.__columnIndex, columnspan=100, padx=10, pady=10)
        self.__rowIndex += 1



    def __initRandom(self) -> None:
        """
        Cette méthode initialise les bouttons de random.
        """
        label = tkinter.Label(self.__menuFrame, text="Random", font="Courier 12", fg="white", bg="black")
        label.grid(row=self.__rowIndex, column=self.__columnIndex, columnspan=100, padx=10, pady=10)
        self.__rowIndex += 1

        self.__randomButton.config(text="Random", font="Courier 12")
        self.__randomButton.grid(row=self.__rowIndex, column=self.__columnIndex, columnspan=3, padx=10, pady=10)
        self.__columnIndex += 2

        range = tkinter.Scale(self.__menuFrame, variable=self.__randomRange, orient=tkinter.HORIZONTAL)
        range.grid(row=self.__rowIndex, column=self.__columnIndex, columnspan=4, padx=10, pady=10)
        self.__columnIndex = 0
        self.__rowIndex += 1



    def setRandomButton(self, func: 'function') -> None:
        """
        Cette méthode modifie la fonction du bouton random.

        param : func - La nouvelle fonction.
        """
        self.__randomButton.config(command=func)



    def __initStartButton(self) -> None:
        """
        Cette méthode initialise les boutons start, stop et reset.
        """
        self.__startButton.config(text="Start", font="Courier 12")
        self.__startButton.grid(row=self.__rowIndex, column=self.__columnIndex, padx=10, pady=10)
        self.__columnIndex += 1

        self.__stopButton.config(text="Stop", font="Courier 12")
        self.__stopButton.grid(row=self.__rowIndex, column=self.__columnIndex, padx=10, pady=10)
        self.__columnIndex += 1

        self.__resetButton.config(text="Reset", font="Courier 12")
        self.__resetButton.grid(row=self.__rowIndex, column=self.__columnIndex, padx=10, pady=10)
        self.__columnIndex += 1



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



    def __initSaveButton(self) -> None:
        """
        Cette méthode initialise les boutons start, stop et reset.

        param : row - La ligne où ça commence.
        param : column - La colonne où ça commence.
        """
        self.__saveButton.config(text="Save", font="Courier 12")
        self.__saveButton.grid(row=self.__rowIndex, column=self.__columnIndex, padx=10, pady=10)
        self.__columnIndex += 1

        self.__importButton.config(text="Import", font="Courier 12")
        self.__importButton.grid(row=self.__rowIndex, column=self.__columnIndex, padx=10, pady=10)



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



    def init(self) -> None:
        """
        Cette méthode initialise l'interface.
        """
        self.__initRoot()
        self.__initCanvas()
        self.__initRender()
        self.__initMenu()
        self.__initTimeRange()
        self.__initRandom()
        self.__initStartButton()
        self.__initSaveButton()



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