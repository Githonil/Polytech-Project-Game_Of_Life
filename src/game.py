import game_of_life_supplement_engine
import game_of_life_graphic

import tkinter
import time
import threading

class Game:
    """
    Cette classe représente le jeu : Game of Life.
    """

    def __init__(self, width : int, height : int, columns : int, rows : int) -> 'Game':
        """
        Le constructeur d'un jeu.

        param : width - La largeur de la fenêtre de la grille.
        param : height - La hauteur de la fenêtre de la grille
        param : columns - Le nombre de colonnes dans la grille.
        param : rows - Le nombre de lignes dans la grille.
        """
        self.__cellsAlive = {}
        self.__columns = columns
        self.__rows = rows
        self.__colors = set()
        self.__lastTickTime = 0
        self.__lastFrameTime = 0
        self.__runningLoop = True
        self.__root = game_of_life_graphic.initRoot()
        self.__tps = tkinter.DoubleVar()
        self.__random = tkinter.IntVar()
        self.__running = [False]
        self.__canvas = game_of_life_graphic.initCanvas(self.__root, width, height)
        self.__elements = {}
        game_of_life_graphic.initRender(self.__canvas, self.__rows, self.__columns)
        self.__menu = game_of_life_graphic.initMenuBase(self.__root)
        game_of_life_graphic.initMenuTPSRange(self.__menu, self.__tps) #TODO: Mettre à jour le graphic.
        game_of_life_graphic.initMenuColor(self.__menu, self.__colors)
        game_of_life_graphic.initMenuRandom(self.__menu, self.__random, self.__cellsAlive, self.__rows, self.__columns, self.__colors)
        game_of_life_graphic.initMenuStartButtons(self.__menu, self.__running, self.__cellsAlive)
        game_of_life_graphic.initMenuSaveButtons(self.__menu, self.__cellsAlive) #TODO: Mettre à jour le graphic.



    def start(self) -> None:
        """
        Cette méthode lance le jeu.
        """
        """
        loop = threading.Thread(target=self.__loop)
        loop.start()
        """
        self.__loop()

        self.__root.mainloop()



    def __stop(self) -> None:
        """
        Cette méthode arrête la boucle du jeu.
        """
        self.__runningLoop = False


    def __loop(self) -> None:
        """
        Cette méthode contient la boucle principale du jeu.
        """
        game_of_life_graphic.initEvent(self.__canvas, self.__cellsAlive, self.__rows, self.__columns, self.__colors)
        self.__root.protocol("WM_DELETE_WINDOW", func=self.__stop)

        while self.__runningLoop:
            if self.__running[0]:
                self.__ticksUpdate(self.__tps.get())
                
            self.__framesUpdate(0) #TODO: Refaire le render car tkinter est codé avec le cul.

        self.__root.destroy()



    def __ticksUpdate(self, ticksPerSecond : int) -> None:
        """
        Cette méthode met à jour les ticks.
        
        param : ticksPerSecond - TPS.
        """
        if (time.time() - self.__lastTickTime <= ticksPerSecond):
            return
            
        game_of_life_supplement_engine.analyze(self.__cellsAlive, self.__rows, self.__columns)
        game_of_life_supplement_engine.update(self.__cellsAlive)
        
        self.__lastTickTime = time.time()



    def __framesUpdate(self, framesPerSecond : int) -> None:
        """
        Cette méthode met à jour les frames.

        param : framesPerSecond - FPS.
        """
        """
        if (time.time() - self.__lastFrameTime <= framesPerSecond):
            return
        """

        game_of_life_graphic.render(self.__root, self.__canvas, self.__elements, self.__cellsAlive, self.__rows, self.__columns)

        self.__lastFrameTime = time.time()