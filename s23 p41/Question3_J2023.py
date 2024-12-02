global Animal #DECLARE Animal : ARRAY[0:19] OF STRING
global Colour #DECLARE Colour : ARRAY[0:9] OF STRING
global AnimalTopPointer #DECLARE AnimalTopPointer : INTEGER
global ColourTopPointer #DECLARE ColourTopPointer : INTEGER
Animal = []
Colour = []
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global AnimalTopPointer
    global Animal
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer -= 1
        return ReturnData

def ReadData():
    try:
        file = open("AnimalData.txt", 'r')
        file2 = open("ColourData.txt", 'r')
        line = file.readline().strip()
        line2 = file2.readline().strip()
        while len(line) > 0:
            PushAnimal(line)
            line = file.readline().strip()
        file.close()
        while len(line2) > 0:
            PushColour(line2)
            line2 = file2.readline().strip()
        file2.close()
    except FileNotFoundError:
        print("File not found")

def PushColour(DataToPush):
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True

def PopColour():
    global ColourTopPointer
    global Colour
    ReturnData = ""
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer-1]
        ColourTopPointer -= 1
        return ReturnData

def OutputItem():
    animal = PopAnimal()
    colour = PopColour()
    if colour == "":
        PushAnimal(animal)
        print(f"No colour")
    elif animal == "":
        PushColour(colour)
        print(f"No animal")
    else:
        print(colour, animal)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()