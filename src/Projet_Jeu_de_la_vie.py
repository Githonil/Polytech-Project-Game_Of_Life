import tkinter
import time

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
    
    
    
def random() -> None:
    """
    Cette fonction ajoute des cellules aléatoirement.
    """
    
    
    
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
    
    
    
def initMenuTimeRange(rootMenu : 'tkinter.Frame', timeDuration : 'tkinter.IntVar') -> None:
    """
    Cette fonction ajoute le temps entre chaque étapes au menu.
    
    param : rootMenu - La racine du menu.
    param : time - Le temps entre chaque étapes.
    """
    menuTimeLabel = tkinter.Label(rootMenu, text="TPS")
    menuTime = tkinter.Scale(rootMenu, from_=1, to_=180, length=100, variable=time, orient = tkinter.HORIZONTAL)
    menuTimeLabel.grid(row=2, column=0, columnspan=5, padx=10, pady=10)
    menuTime.grid(row=3, column=0, columnspan=5, padx=10, pady=10)
    
    
    
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
    print(colors)
    
    
def initMenuColor(rootMenu : 'tkinter.Frame', colors : set) -> None:
    """
    Cette fonction ajoute les boutons de couleurs au menu.
    
    param : rootMenu - La racine du menu.
    param : color - La liste des couleurs actives.
    """
    redButton = tkinter.Checkbutton(rootMenu, bg="red", width=3, command=lambda : updateColor(colors, "red"))
    blueButton = tkinter.Checkbutton(rootMenu, bg="blue", width=3, command=lambda : updateColor(colors, "blue"))
    greenButton = tkinter.Checkbutton(rootMenu, bg="green", width=3, command=lambda : updateColor(colors, "green"))
    redButton.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    blueButton.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
    greenButton.grid(row=4, column=2, columnspan=3, padx=10, pady=10)
    
    
    
def initMenuRandom(rootMenu : 'tkinter.Frame', randomValue : 'tkinter.IntVar') -> None:
    """
    Cette fonction ajoute les boutons random au menu.
    
    param : rootMenu - La racine du menu.
    param : randomValue - La valeur du random.
    """
    menuRandom = tkinter.Button(rootMenu, text="random")
    menuRandomRange = tkinter.Scale(rootMenu, from_=1, to_=100, length=50, variable=randomValue, orient = tkinter.HORIZONTAL)
    menuRandom.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    menuRandomRange.grid(row=5, column=2, columnspan=3, padx=10, pady=10)
    
    
    
def initMenuStartButtons(rootMenu : 'tkinter.Frame') -> None:
    """
    Cette fonction ajoute les boutons start et stop au menu.
    
    param : rootMenu - La racine du menu.
    """
    menuStart = tkinter.Button(rootMenu, text="Start")
    menuStop = tkinter.Button(rootMenu, text="Stop")
    menuReset = tkinter.Button(rootMenu, text="Reset")
    menuStart.grid(row=6, column=0, padx=10, pady=10)
    menuStop.grid(row=6, column=1, padx=10, pady=10)
    menuReset.grid(row=6, column=2, padx=10, pady=10)
    
    
    
def initMenuSaveButtons(rootMenu : 'tkinter.Frame') -> None:
    """
    Cette fonction ajoute les boutons de sauvegarde et d'importation au menu.
    
    param : rootMenu - La racine du menu.
    """
    menuSave = tkinter.Button(rootMenu, text="Save")
    menuImport = tkinter.Button(rootMenu, text="Import")
    menuSave.grid(row=6, column=3, padx=10, pady=10)
    menuImport.grid(row=6, column=4, padx=10, pady=10)
    
    
    
def changeColor(cellAlives : dict, x : int, y : int, oldColor : str, newColor) -> None:
    """
    Cette fonction change la couleur si elle a l'ancienne couleur alors elle la remplace par la nouvelle.
    
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : x - La composante X de la coordonnée de la cellule.
    param : y - La composante Y de la coordonnée de la cellule.
    param : oldColor - L'ancienne couleur.
    param : newColor - La nouvelle couleur.
    """
    if cellAlives[(x, y)][0] == oldColor:
        cellAlives[(x, y)][0] == newColor
    
    
    
def clickCell(event : 'tkinter.Event', cellAlives : dict, cellWidth : int, cellHeight : int, colors : set) -> None:
    """
    Cette fonction agit lorsque l'utilisateur click sur une cellule.
    
    param : event - Le registre de l'évènement.
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : columns - Le nombre de colonnes.
    param : rows - Le nombre de lignes.
    param : colors - La liste des couleurs actives.
    """
    coordX = (event.x - (event.x%cellWidth)) / cellWidth
    coordY = (event.y - (event.y%cellHeight)) / cellHeight
    print(coordX, " et ", coordY)
    
    if (coordX, coordY) in cellAlives:
        changeColor(cellAlives, coordX, coordY, "red", "blue")
        changeColor(cellAlives, coordX, coordY, "blue", "green")
        changeColor(cellAlives, coordX, coordY, "green", "white")
    else:
        addCell(cellAlives, coordX, coordY, "red", 0)
    
    
    
def initEvent(canvas : 'tkinter.Canvas', cellAlives : dict, columns : int, rows : int, colors : set) -> None:
    """
    Cette fonction initialise les évènements.
    
    param : Le canvas de l'interface.
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : columns - Le nombre de colonnes.
    param : rows - Le nombre de lignes.
    param : colors - La liste des couleurs actives.
    """
    canvasWidth = int(canvas.cget("width"))
    canvasHeight = int(canvas.cget("height"))
    
    cellWidth = canvasWidth // columns
    cellHeight = canvasHeight // rows
    
    canvas.bind('<Button-1>', lambda event: clickCell(event, cellAlives, cellWidth, cellHeight, colors))
    
    
    
def render(canvas : 'tkinter.Canvas', cellAlives : dict, columns : int, rows : int) -> None:
    """
    Cette fonction calcule le rendu du canvas.
    
    param : canvas - Le canvas de l'interface graphique.
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : columns - Le nombre de colonnes.
    param : rows - Le nombre de lignes.
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
        
        
    
    for cellCoord in cellAlives:
        coordX = cellCoord[0] * cellWidth
        coordY = cellCoord[1] * cellHeight
        canvas.create_rectangle(coordX, coordY, coordX + cellWidth - 1, coordY + cellHeight - 1, fill=cellAlives[cellCoord][0])
    
    

def addCell(cellAlives : dict, x : int, y : int, color : str, lifeTime : int) -> None:
    """
    Cette fonction ajoute une cellule dans les cellules vivantes.
    
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : x - La composante X de la coordonnée de la cellule.
    param : y - La composante Y de la coordonnée de la cellule.
    param : color - La couleur de la cellule.
    param : lifeTime - Le temps de vie de la cellule.
    """
    cellAlives[(x, y)] = [color, lifeTime, 0]
    
    
    
def removeCell(cellAlives : dict, x : int, y : int) -> None:
    """
    Cette fonction supprime une cellule dans les cellules vivantes.
    
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines]
    param : x - La composante X de la coordonnée de la cellule.
    param : y - La composante Y de la coordonnée de la cellule.
    """
    del cellAlives[(x, y)]
    
    

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
    
    
    
def analyze(cellAlives : dict, newBorns : dict, width : int, height : int) -> None:
    """
    Cette fonction analyse les cellules vivantes.
    
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : newBorns - Le conteneur qui contient toutes les futures cellules vivantes. Même structure que pour cellAlives.
    param : width - La largeur de la grille.
    param : height - La hauteur de la grille.
    """
    newBorns.clear()
    futureBorns = {}
    
    for cellCoord in cellAlives:
        cellAlives[cellCoord][2] = 0
    
        for y in range(-1, 2):
            for x in range(-1, 2):
                
                if x == 0 and y == 0:
                    continue
                    
                coordX = x + cellCoord[0]
                coordY = y + cellCoord[1]
                
                adjustBorder(coordX, width)
                adjustBorder(coordY, height)
                
                if (coordX, coordY) in cellAlives and cellAlives[(coordX, coordY)][0] == cellAlives[cellCoord][0]:
                    cellAlives[cellCoord][2] += 1
                    
                elif not (coordX, coordY) in cellAlives:
                
                    if not (coordX, coordY) in futureBorns:
                        parent = cellAlives[(cellCoord[0], cellCoord[1])]
                        futureBorns[(coordX, coordY)] = [parent[0], parent[1], 0]
                        
                    futureBorns[(coordX, coordY)][2] += 1
                    
    for newCellCoord in futureBorns:
        if futureBorns[newCellCoord][2] == 3:
            newBorns[newCellCoord] = futureBorns[newCellCoord]
            
            
            
def update(cellAlives : dict, newBorns : dict) -> None:
    """
    Cette fonction met à jour toutes les cellules.
    
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : newBorns - Le conteneur qui contient toutes les futures cellules vivantes. Même structure que pour cellAlives.
    """
    cellKeys = list(cellAlives.keys()).copy()
    for cellCoord in cellKeys:
        if cellAlives[cellCoord][2] != 2 and cellAlives[cellCoord][2] != 3:
            removeCell(cellAlives, cellCoord[0], cellCoord[1])
            
    for newCellCoord in newBorns:
        cell = newBorns[newCellCoord]
        addCell(cellAlives, newCellCoord[0], newCellCoord[1], cell[0], cell[1])



def ticksUpdate(ticksPerSecond : int, lastTickTime : float, cellAlives : dict, newBorns : dict, width : int, height : int) -> int:
    """
    Cette fonction met à jour les ticks.
    
    param : ticksPerSecond - 
    param : lastTick - Le temps du dernier tick.
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : newBorns - Le conteneur qui contient toutes les futures cellules vivantes. Même structure que pour cellAlives.
    param : width - La largeur de la grille.
    param : height - La hauteur de la grille.
    return : Renvoie le nouveau temps du dernier tick.
    """
    if (time.time() - lastTickTime <= ticksPerSecond):
        return lastTickTime
        
    analyze(cellAlives, newBorns, width, height)
    update(cellAlives, newBorns)
    
    print(cellAlives)
    
    return time.time()
    



def main() -> None:
    """
    La fonction principale.
    """
    cellAlives = {} #Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    newBorns = {} #Même structure que cellAlives. Contient les futures cellules vivantes.
    width = 72
    height = 52
    colors = set()
    
    lastTickTime = time.time()
    
    
    root = initRoot()
    canvas = initCanvas(root, 720, 520)
    menu = initMenuBase(root)
    initMenuTimeRange(menu, tkinter.IntVar())
    initMenuColor(menu, colors)
    initMenuRandom(menu, tkinter.IntVar())
    initMenuStartButtons(menu)
    initMenuSaveButtons(menu)
    initEvent(canvas, cellAlives, width, height, colors)
    render(canvas, cellAlives, width, height)
    root.mainloop()
    
    
    while False:
        
        lastTickTime = ticksUpdate(0.1, lastTickTime, cellAlives, newBorns, width, height)
    
    
    
main()