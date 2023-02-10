import tkinter
import time

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



def ticksUpdate(ticksPerSecond : int, lastTickTime : float, width : int, height : int cellAlives : dict, newBorns) -> int:
    """
    Cette fonction met à jour les ticks.
    
    param : ticksPerSecond - 
    param : lastTick - Le temps du dernier tick.
    param : width - La largeur de la grille.
    param : height - La hauteur de la grille.
    param : cellAlives - Le conteneur qui contient toutes les cellules vivantes. Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    param : newBorns - Le conteneur qui contient toutes les futures cellules vivantes. Même structure que pour cellAlives.
    return : Renvoie le nouveau temps du dernier tick.
    """
    if (time.time() - lastTickTime <= ticksPerSecond):
        return lastTickTime
        
    analyze(cellAlives, newBorns, width, height)
    update(cellAlives, newBorns)
    
    return time.time()
    



def main() -> None:
    """
    La fonction principale.
    """
    cellAlives = {} #Clef leur coordonnée : (x, y) et la valeur : [couleur, temps de vie, nombre de cases voisines].
    newBorns = {} #Même structure que cellAlives. Contient les futures cellules vivantes.
    width = 10
    height = 10
    
    lastTickTime = time.time()
    
    while True:
        
        lastTickTime = ticksUpdate(0.1, lastTickTime, width, height, cellAlives, newBorns)
    
    
    
main()