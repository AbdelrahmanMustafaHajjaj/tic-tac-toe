import re 
class Player: 
    def __init__(self)->None:
        self.__symbol: str = ""
        self.__name: str = ""
    def chooseName(self)->None:
        namePattern:str = "[a-zA-Z]+$"
        while True:
            name:str  = input("Enter the player name[Enter only alphapetic charcters]: ").strip()
            if re.match(namePattern,name):
                self.__name = name 
                break 

    def chooseSymbol(self)->None :
        symbolPattern:str = "[a-zA-Z]{1}$"
        while True :
            symbol:str  = input("Enter the player symbol[only input a single character]: ").strip()
            if re.match(symbolPattern,symbol):
                self.__symbol = symbol.upper() 
                break 
    @property
    def name(self):
        return self.__name
    @property 
    def symbol(self):
        return self.__symbol
    def __eq__(self,other):
        return self.symbol == other.symbol

            

