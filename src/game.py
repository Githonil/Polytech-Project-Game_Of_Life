import game_of_life_supplement_engine
import game_of_life_supplement_graphic

import time

class GameOfLife:
    """
    Cette classe représente le jeu : Game of Life.
    Ajout du jeu:
    - Des couleurs aux cellules.
    """

    def __init__(self, width : int, height : int, columns : int, rows : int) -> 'GameOfLife':
        """
        Le constructeur d'un jeu.

        param : width - La largeur de la fenêtre de la grille.
        param : height - La hauteur de la fenêtre de la grille
        param : columns - Le nombre de colonnes dans la grille.
        param : rows - Le nombre de lignes dans la grille.
        """
        self.__columns = columns
        self.__rows = rows
        self.__cellsAlive = {}
        self.__graphic = game_of_life_supplement_graphic.GameOfLifeGraphic(width, height, columns, rows)
        self.__graphic.init()
        self.__graphic.initQuitButton(self.__stop)
        self.__init()
        self.__running = False
        self.__mainLoop = True
        self.__lastTickTime = time.time()
        self.__lastFrameTime = time.time()



    def __initRandomButton(self) -> None:
        """
        Cette méthode initialise le bouton random.
        """
        import random
        import math

        colors = self.__graphic.colorsSet
        if len(colors) == 0:
            return
        
        numberCells = math.ceil((self.__rows * self.__columns - len(self.__cellsAlive)) *  (self.__graphic.getRandomRange() / 100))

        for i in range(numberCells):
            coordX = random.randint(0, self.__columns - 1)
            coordY = random.randint(0, self.__rows - 1)

            while (coordX, coordY) in self.__cellsAlive:
                coordX = random.randint(0, self.__columns - 1)
                coordY = random.randint(0, self.__rows - 1)

            color = random.choice(list(colors))

            game_of_life_supplement_engine.addCell(self.__cellsAlive, coordX, coordY, color)



    def __initStartButton(self) -> None:
        """
        Cette méthode initialise le bouton start.
        """
        self.__running = True



    def __initStopButton(self) -> None:
        """
        Cette méthode initialise le bouton stop.
        """
        self.__running = False



    def __initResetButton(self) -> None:
        """
        Cette méthode initialise le bouton reset.
        """
        self.__running = False
        self.__cellsAlive.clear()



    def __initSaveButton(self) -> None:
        """
        Cette méthode initialise le bouton save.
        """
        game_of_life_supplement_graphic.GameOfLifeGraphic.save(self.__cellsAlive)



    def __initImportButton(self) -> None:
        """
        Cette méthode initialse le bouton import.
        """
        self.__cellsAlive = game_of_life_supplement_graphic.GameOfLifeGraphic.import_obj()


    def __init(self) -> None:
        """
        Cette méthode initialise les butons.
        """
        self.__graphic.setRandomButton(self.__initRandomButton)
        self.__graphic.setStartButton(self.__initStartButton)
        self.__graphic.setStopButton(self.__initStopButton)
        self.__graphic.setResetButton(self.__initResetButton)
        self.__graphic.setSaveButton(self.__initSaveButton)
        self.__graphic.setImportButton(self.__initImportButton)



    def start(self) -> None:
        """
        Cette méthode lance le jeu.
        """
        self.__loop()



    def __stop(self) -> None:
        """
        Cette méthode arrête la boucle du jeu.
        """
        self.__mainLoop = False



    def __event(self, oldX, oldY) -> tuple:
        """
        Cette méthode gère les évènements.

        param : oldX - La composante X de l'ancienne coordonnée.
        param : oldY - La composante Y de l'ancienne coordonnée.
        return : Renvoie la nouvelle coordonnée (coordX, coordY).
        """
        colors_size = len(self.__graphic.colorsSet)
        colors = sorted(list(self.__graphic.colorsSet))
        colors.reverse()

        coordX, coordY = self.__graphic.getMouseX(), self.__graphic.getMouseY()

        if (coordX == -1 and coordY == -1):
            return (oldX, oldY)

        if self.__graphic.motionDetect and oldX == coordX and oldY == coordY:
            self.__graphic.motionDetect = False
            return (oldX, oldY)

        if self.__graphic.eventDetect and (coordX, coordY) in self.__cellsAlive:
            if colors_size == 0:
                game_of_life_supplement_engine.removeCell(self.__cellsAlive, coordX, coordY)
                self.__graphic.eventDetect = False
                return (coordX, coordY)

            cell = self.__cellsAlive[(coordX, coordY)]
            index = 0
            try:
                index = colors.index(cell.color)
            except:
                index = -1

            if index != colors_size - 1:
                cell.color = colors[index + 1]
            else:
                game_of_life_supplement_engine.removeCell(self.__cellsAlive, coordX, coordY)


        elif self.__graphic.eventDetect and colors_size > 0:
            game_of_life_supplement_engine.addCell(self.__cellsAlive, coordX, coordY, colors[0])
            
        self.__graphic.eventDetect = False

        return (coordX, coordY)



    def __loop(self) -> None:
        """
        Cette méthode contient la boucle principale du jeu.
        """
        oldX = -1
        oldY = -1
        while self.__mainLoop:

            oldX, oldY = self.__event(oldX, oldY)

            self.__framesUpdate(1/60)

            if self.__running:
                self.__ticksUpdate(self.__graphic.getTimeRange())



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
        if (time.time() - self.__lastFrameTime <= framesPerSecond):
            return

        self.__graphic.render({k : v.color for k, v in self.__cellsAlive.items()})

        self.__lastFrameTime = time.time()