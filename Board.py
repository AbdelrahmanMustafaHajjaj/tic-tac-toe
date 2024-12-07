class Board :
    def __init__(self)->None:
        self.baordList = [str(i) for i in range(1,10)]

    def displayBoard(self):
       for i in range(0,len(self.baordList),3):
           print("|".join(self.baordList[i:i+3]))
           if i < 6:
            print("-"*5)

    def isValid(self,choice:int):
       try:
        return self.baordList[choice-1].isdigit()
       except (IndexError,ValueError) as e :
          print(f"{e}: invalid move")
          return False
    
          
    def updateBoard(self,choice:int,symbol:str):
        if self.isValid(choice):
           self.baordList[choice-1] = symbol.upper() 
           return True
        return False 
    
    def resetBoard(self):
       self.baordList = [str(i) for i in range(1,10)]
