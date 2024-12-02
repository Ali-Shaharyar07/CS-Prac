class Picture:
    #DECLARE PRIVATE Description : STRING
    #DECLARE PRIVATE Width : INTEGER
    #DECLARE PRIVATE Height : INTEGER
    #DECLARE PRIVATE FrameColour : STRING

    def __init__(self, desc, w, h, color):
        self.__Description = desc
        self.__Width = w
        self.__Height = h
        self.__FrameColour = color

    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetFrameColour(self):
        return self.__FrameColour

    def SetDescription(self, desc):
        self.__Description = desc

Pictures = [Picture("",0,0,"") for i in range(100)]
#ADD TRY CATCH

def ReadData():
    global Pictures
    try:
        file = open("Pictures.txt", 'r')
        line = file.readline().strip()
        c = 0
        i = 0
        while (len(line)>0):
            if c == 0:
                desc = line
            elif c == 1:
                width = int(line)
            elif c == 2:
                height = int(line)
            else:
                colour = line
                Pictures[i] = Picture(desc, width, height, colour)
                i += 1 # max index + 1 -> total pics = i-2
                c = -1
            c += 1
            line = file.readline().strip()
        file.close()
        return i
    except FileNotFoundError:
        print("File not Found")

num = ReadData()
#print(num)
uC = input("Enter required colour: ").lower()
uW = int(input("Enter maximum width: "))
uH = int(input("Enter maximum Height: "))


for e in Pictures:
    w = int(e.GetWidth())
    h = int(e.GetHeight())
    c = e.GetFrameColour()

    if w <= uW and h <= uH and c == uC:
        print(f"Description: {e.GetDescription()}, width: {w}, height: {h}")



