import sys
class Menu:
    def __init__(self,listOfchoice:list,openingsentence:str)->None:
        self.openingSentence:str = openingsentence
        self.listOfChoice:list = listOfchoice
        self.menuLen:int = len(self.listOfChoice)
    def displayMenu(self)->None:
        print(self.openingSentence)
        for  index,value  in enumerate(self.listOfChoice,start=1):
            print(index,value)
    def getInput(self)->str:
        self.displayMenu()
        try:
            choice:int = int(input("Enter the number of choice : ").strip())
            while choice not in range(1,self.menuLen+1) :
                choice = int(input("EnterEnter a valid number  : ").strip())
            
        except ValueError:
            print("you can only write integer number")
            sys.exit()
        return self.listOfChoice[choice-1] 