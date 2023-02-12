import game

def main() -> None:
    """
    La fonction principale.
    """
    gameMotor = game.Game(720, 520, 72, 52)
    gameMotor.start()



if __name__ == '__main__':
    main()