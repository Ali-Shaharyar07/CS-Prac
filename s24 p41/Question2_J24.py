class Tree:
    #DECLARE PRIVATE TreeName : STRING
    #DECLARE PRIVATE HeightGrowth : INTEGER
    #DECLARE PRIVATE MaxHeight : INTEGER
    #DECLARE PRIVATE MaxWidth : INTEGER
    #DECLARE PRIVATE Evergreen : STRING

    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName
        self.__HeightGrowth = HeightGrowth
        self.__MaxHeight = MaxHeight
        self.__MaxWidth = MaxWidth
        self.__Evergreen = Evergreen

    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen

#2D array -> array ( (0 for i in range(3)) for c in range (10) ) inner columns -> outer rows
def ReadData():
    #DECLARE trees : ARRAY OF Tree
    #DECLARE c : INTEGER
    #DECLARE commas, obj : ARRAY[0:4] OF INTEGER
    #DECLARE lines : STRING
    #DECALRE char : CHAR

    trees = [] # [(tree1 height, name) , (tree2 height, name) ]
    try:
        file = open("Trees.txt", 'r') #r for Read, w for Write, a for Append
        lines = file.readline().strip()
        c = 0
        commas = [0,0,0,0]
        while len(lines) > 0:
            for i in range(0, len(lines)):
                char = lines[i]
                if char == ',':
                    commas[c] = i
                    c += 1
            c = 0
            obj = Tree(lines[:commas[0]], #SP -> inclusive EP is exclusive
                       lines[commas[0]+1:commas[1]],
                       lines[commas[1]+1:commas[2]],
                       lines[commas[2]+1:commas[3]],
                       lines[commas[3]+1:])
            trees.append(obj)
            lines = file.readline().strip()
        file.close()
        return trees
    except FileNotFoundError:
        print("File not Found")


def PrintTrees(obj):
    #DECLARE height, width, growth : INTEGER
    #DECLARE evergreen : BOOLEAN
    #DECLARE name : STRING

    height, width, growth = 0, 0, 0
    evergreen = False
    name = ""

    name = obj.GetTreeName()
    height = obj.GetMaxHeight()
    width = obj.GetMaxWidth()
    growth = obj.GetGrowth()
    evergreen = obj.GetEvergreen()

    if evergreen:
        print(f"{name} has a maximum height of {height} a maximum width of {width} and grows {growth}cm a year. It does not loses its leaves each year")
    else:
        print(f"{name} has a maximum height of {height} a maximum width of {width} and grows {growth}cm a year. It loses its leaves each year")

TreeList = ReadData()
#PrintTrees(TreeList[0])

def ChooseTrees(arr):
    #DECLARE maxH, maxW, h, w, cH : INTEGER
    #DECLARE evergreen, e, response : STRING


    chosen = []

    maxH = int(input("Enter max height in cm: "))
    maxW = int(input("Enter max width in cm: "))
    evergreen = input("Is tree evergreen? (Yes/No): ")

    for element in arr:
        h = int(element.GetMaxHeight())
        w = int(element.GetMaxWidth())
        e = element.GetEvergreen()
        #print(f"{h} {w} {e}")
        if (h < maxH) and (w < maxW) and (e == evergreen):
            chosen.append(element)

    if (len(chosen) == 0):
        print("No tree matches requirements")
    else:
        for tree in chosen:
            PrintTrees(tree)
        response = input("Enter name to buy: ")
        cH = int(input("Enter current height: "))
        for tree in chosen:
            if tree.GetTreeName() == response:
                time = (int(tree.GetMaxHeight())-cH)/int(tree.GetGrowth())
                print(f"It will take {time} years for {tree.GetTreeName()} grow to {tree.GetMaxHeight()}")


ChooseTrees(TreeList)
