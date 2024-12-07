import Player, Menu,Board
import os ,sys
def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")
def equals(numbers):
    ele = numbers[0]
    for i in numbers :
        if i != ele :
            return False 
    return True 


class Game :
    def __init__(self):
        self.players:list = [Player.Player(),Player.Player()]
        self.board:object     = Board.Board()
        mainMenuList:list     = ["START GAME","QUIT THE GAME"]
        endMenuList:list      = ["RESTART GAME","QUIT THE GAME"]
        self.mainMenu:object  = Menu.Menu(mainMenuList,"WELCOME IN THE GAME")
        self.endMenu:object   = Menu.Menu(endMenuList,"YOU ARE DOING WELL LET'S START ANOTHER GAME")
        self.playerIndex:int  = 0
    def checkPlayerEquality(self):
        return (self.players[0] == self.players[1])
    def startGame(self):
        if self.mainMenu.getInput() == "START GAME" : 
            self.setupPlayer()
            self.playGame()
        else :
            self.endGame()
    def setupPlayer(self):
        for index,player in enumerate(self.players,start= 1):
            print(f"player {index} Enter your details")
            player.chooseName() 
            player.chooseSymbol()
            clearScreen()
        try:
            if self.checkPlayerEquality():
                raise ValueError
        except ValueError :
            print("player's symbols are equal")
            sys.exit(0)
            
    def playGame(self):
        while True :
            self.playTurn()
            if self.checkWin() or self.checkDraw() :
                if self.endMenu.getInput() == "RESTART GAME":
                    self.restartGame()
                else :
                    self.endGame()
            
            # self.board.updateBoard()

    def restartGame(self):
        self.board.resetBoard()
        self.playerIndex = 0 
        self.playGame()

    def playTurn(self):
        player = self.players[self.playerIndex]
        self.board.displayBoard()
        print(f"{player.name} it's you turn")
        while True :
            choice = int(input("choose a cell (1:9): "))
            if self.board.updateBoard(choice, player.symbol):
                break
        self.switchPlayer()
    
    def switchPlayer(self):
        self.playerIndex = 1 - self.playerIndex 
        

    def checkWin(self):
        
        win_combinations = [
            
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            line = [self.board.baordList[i] for i in combo]
            if equals(line):
                winner = self.players[0] if line[0] == self.players[0].symbol else self.players[1]
                print(f"{winner.name} is the winner")
                return True

        return False
             
    def alpha(self,char):
        return char.isalpha()
    


    def checkDraw(self):
        if all(not cell.isdigit() for cell in self.board.baordList):
            print("Draw")
            return True 
        return False 



    def endGame(self):
        print("Thank You for Playing!")
        sys.exit()
game = Game()
game.startGame()    
   