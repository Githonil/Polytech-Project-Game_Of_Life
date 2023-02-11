import game_of_life_supplement_engine

import tkinter

def initRoot() -> 'tkinter.Tk':
    """
    Cette fonction initialise l'interface graphique.
    
    return : Renvoie la racine de l'interface.
    """
    root = tkinter.Tk()
    root.title("Game of Life")
    root.config(bg="black")
    
    return root
    
    
    
def initCanvas(root : 'tkinter.Tk', width : int, height : int) -> 'tkinter.Canvas':
    """
    Cette fonction initialise le canvas de l'interface graphique.
    
    param : root - La racine de l'interface.
    param : width - La largeur du canvas.
    param : height - La hauteur du canvas.
    return : Renvoie le canvas de l'interface.
    """
    canvas = tkinter.Canvas(root, width=width, height=height, bg="white")
    canvas.grid(row=0, column=0)
    
    return canvas
    
    
    
def initMenuBase(root : 'tkinter.Tk') -> 'tkinter.Frame':
    """
    Cette fonction initialise le menu de l'interface graphique.
    
    param : root - La racine de l'interface.
    return : Renvoie la racine du menu.
    """
    frame = tkinter.Frame(root, bg="black")
    frame.grid(row=0, column=1)
    
    title = tkinter.Label(frame, text="Game of Life")
    title.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
    
    return frame
    
    
    
"""    
def initMenuLifeRange(rootMenu : 'tkinter.Frame', lifeDuration : 'tkinter.IntVar') -> None:
    
    Cette fonction ajoute le temps de vie d'une cellule au menu.
    
    param : rootMenu - La racine du menu.
    param : lifeDuration - Le temps de vie d'une cellule.
    
    menuLifeLabel = tkinter.Label(rootMenu, text="Temps de vies d'une cellule")
    menuLife = tkinter.Scale(rootMenu, from_=1, to_=60, length=100, variable=lifeDuration, orient = tkinter.HORIZONTAL)
    menuLifeLabel.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
    menuLife.grid(row=2, column=0, columnspan=5, padx=10, pady=10)
"""
    
    
    
def initMenuTPSRange(rootMenu : 'tkinter.Frame', timeDuration : 'tkinter.IntVar') -> None:
    """
    Cette fonction ajoute le temps entre chaque étapes au menu.
    
    param : rootMenu - La racine du menu.
    param : timeDuration - Le temps entre chaque étapes.
    """
    timeLabel = tkinter.Label(rootMenu, text="TPS")
    timeRange = tkinter.Scale(rootMenu, from_=1, to_=180, length=100, variable=timeDuration, orient = tkinter.HORIZONTAL)
    timeLabel.grid(row=2, column=0, columnspan=5, padx=10, pady=10)
    timeRange.grid(row=3, column=0, columnspan=5, padx=10, pady=10)
    
    
    
def updateColor(colors: set, color : str) -> None:
    """
    Cette fonction met à jour la liste des couleurs actives.
    Si la couleur n'est pas dans la liste, elle la retire.
    Sinon elle l'enlève.
    
    param : colors - La liste des couleurs actives.
    param : color - La couleur à analyser.
    """
    if color in colors:
        colors.remove(color)
    else:
        colors.add(color)
    
    
    
def initMenuColor(rootMenu : 'tkinter.Frame', colors : set) -> None:
    """
    Cette fonction ajoute les boutons de couleurs au menu.
    
    param : rootMenu - La racine du menu.
    param : color - La liste des couleurs actives.
    """
    redButton = tkinter.Checkbutton(rootMenu, bg="red", width=3, command=lambda : updateColor(colors, "red"))
    greenButton = tkinter.Checkbutton(rootMenu, bg="green", width=3, command=lambda : updateColor(colors, "green"))
    blueButton = tkinter.Checkbutton(rootMenu, bg="blue", width=3, command=lambda : updateColor(colors, "blue"))
    redButton.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    greenButton.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
    blueButton.grid(row=4, column=2, columnspan=3, padx=10, pady=10)
    
    
    
def initMenuRandom(rootMenu : 'tkinter.Frame', randomValue : 'tkinter.IntVar') -> None:
    """
    Cette fonction ajoute les boutons random au menu.
    
    param : rootMenu - La racine du menu.
    param : randomValue - La valeur du random.
    """
    randomButton = tkinter.Button(rootMenu, text="random")
    randomRange = tkinter.Scale(rootMenu, from_=1, to_=100, length=50, variable=randomValue, orient = tkinter.HORIZONTAL)
    randomButton.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    randomRange.grid(row=5, column=2, columnspan=3, padx=10, pady=10)
    
    
    
def initMenuStartButtons(rootMenu : 'tkinter.Frame') -> None:
    """
    Cette fonction ajoute les boutons start et stop au menu.
    
    param : rootMenu - La racine du menu.
    """
    startButton = tkinter.Button(rootMenu, text="Start")
    stopButton = tkinter.Button(rootMenu, text="Stop")
    resetButton = tkinter.Button(rootMenu, text="Reset")
    startButton.grid(row=6, column=0, padx=10, pady=10)
    stopButton.grid(row=6, column=1, padx=10, pady=10)
    resetButton.grid(row=6, column=2, padx=10, pady=10)
    
    
    
def initMenuSaveButtons(rootMenu : 'tkinter.Frame') -> None:
    """
    Cette fonction ajoute les boutons de sauvegarde et d'importation au menu.
    
    param : rootMenu - La racine du menu.
    """
    saveButton = tkinter.Button(rootMenu, text="Save")
    importButton = tkinter.Button(rootMenu, text="Import")
    saveButton.grid(row=6, column=3, padx=10, pady=10)
    importButton.grid(row=6, column=4, padx=10, pady=10)



def clickCell(event : 'tkinter.Event', cellsAlive : dict, cellWidth : int, cellHeight : int, colors : set) -> None:
    """
    Cette fonction agit lorsque l'utilisateur click sur une cellule.
    
    param : event - Le registre de l'évènement.
    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : cellWidth - La largeur d'une cellule.
    param : cellHeight - La hauteur d'une cellule.
    param : colors - La liste des couleurs actives.
    """
    coordX = (event.x - (event.x%cellWidth)) / cellWidth
    coordY = (event.y - (event.y%cellHeight)) / cellHeight

    colors = sorted(colors).reverse()
    colors_size = len(colors)
    
    if (coordX, coordY) in cellsAlive:
        cell = cellsAlive[(coordX, coordY)]
        index = colors.index(cell.color)

        if index == colors_size - 1:
            game_of_life_supplement_engine.removeCell(cellsAlive, coordX, coordY)
        else:
            cell.color = colors[index + 1]

    elif colors_size != 0:
        game_of_life_supplement_engine.addCell(cellsAlive, coordX, coordY, "red")
    
    
    
def initEvent(canvas : 'tkinter.Canvas', cellsAlive : dict, rows : int, columns : int, colors : set) -> None:
    """
    Cette fonction initialise les évènements.
    
    param : Le canvas de l'interface.
    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : rows - Le nombre de lignes.
    param : columns - Le nombre de colonnes.
    param : colors - La liste des couleurs actives.
    """
    canvasWidth = int(canvas.cget("width"))
    canvasHeight = int(canvas.cget("height"))
    
    cellWidth = canvasWidth // columns
    cellHeight = canvasHeight // rows
    
    canvas.bind('<Button-1>', lambda event: clickCell(event, cellsAlive, cellWidth, cellHeight, colors))



def render(canvas : 'tkinter.Canvas', cellsAlive : dict, rows : int, columns : int) -> None:
    """
    Cette fonction calcule le rendu du canvas.
    
    param : canvas - Le canvas de l'interface graphique.
    param : cellsAlive - Contient toutes les cellules vivantes. Clef : (x, y) ; Valeur : Cell.
    param : rows - Le nombre de lignes.
    param : columns - Le nombre de colonnes.
    """
    canvasWidth = int(canvas.cget("width"))
    canvasHeight = int(canvas.cget("height"))
    
    cellWidth = canvasWidth // columns
    cellHeight = canvasHeight // rows
    
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill="white")
    
    
    for column in range(columns):
        coordX = cellWidth * (column + 1)
        canvas.create_rectangle(coordX, 0, coordX + 1, canvasHeight, fill="black")
        
        
    for row in range(rows):
        coordY = cellHeight * (row + 1)
        canvas.create_rectangle(0, coordY, canvasWidth, coordY + 1, fill="black")
        
    
    for cellCoord in cellsAlive:
        coordX = cellCoord[0] * cellWidth
        coordY = cellCoord[1] * cellHeight
        canvas.create_rectangle(coordX, coordY, coordX + cellWidth - 1, coordY + cellHeight - 1, fill=cellsAlive[cellCoord].color)