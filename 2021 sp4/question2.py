class HiddenBox:
    #DECLARE PRIVATE BoxName : STRING
    #DECLARE PRIVATE Creator : STRING
    #DECLARE PRIVATE DateHidden : STRING
    #DECLARE PRIVATE GameLocation : STRING
    #DECLARE PRIVATE LastFinds : ARRAY[0:9, [0:1]] OF STRING
    #DECLARE PRIVATE Active : BOOLEAN

    def __init__(self, n, c, d, l):
        self.__BoxName = n
        self.__Creator = c
        self.__DateHidden = d
        self.__GameLocation = l
        self.__Active = False
        self.LastFinds = [["", ""] for i in range(10)]

    def GetBoxName(self):
        return self.__BoxName
    def GetNameLocation(self):
        return self.__GameLocation

TheBoxes = [] #DECLARE TheBoxes : ARRAY[0:9999] OF HiddenBox

def NewBox():
    name = input("Enter name: ")
    creator = input("Enter creator: ")
    date = input("Enter date: ")
    loc = input("Enter location: ")
    TheBoxes.append(HiddenBox(name, creator, date, loc))

NewBox()

class PuzzleBox(HiddenBox):
    #DECLARE PRIVATE PuzzleText : STRING
    #DECLARE PRIVATE Solution : STRING

    def __init__(self, n, c, d, l, p, s):
        HiddenBox.__init__(self, n, c, d, l)
        self.__PuzzleText = p
        self.__Solution = s
