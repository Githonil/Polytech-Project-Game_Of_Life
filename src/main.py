import game

def main() -> None:
    """
    La fonction principale.
    """
    gameMotor = game.GameOfLife(720, 520, 72, 52)
    gameMotor.start()



if __name__ == '__main__':
    main()