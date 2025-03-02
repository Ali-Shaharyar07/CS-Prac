ArrayNodes = [[-1, -1, -1] for i in range(20)]
RootPointer = -1
FreeNode = 0

def AddNode():
    global ArrayNodes, RootPointer, FreeNode
    NodeData = int(input("Enter the data: "))

    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1

        if RootPointer == -1: RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode += 1
    else:
        print("Tree is full")

def PrintAll():
    global ArrayNodes
    for e in ArrayNodes:
        if e[1] != -1:
            print(f"{e[0]} {e[1]} {e[2]}")

for i in range(10):
    AddNode()
#PrintAll()

def InOrder(Array, RootPtr):
    if Array[RootPtr][0] != -1:
        InOrder(Array, Array[RootPtr][0])
    print(Array[RootPtr][1])
    if Array[RootPtr][2] != -1:
        InOrder(Array, Array[RootPtr][2])

InOrder(ArrayNodes, RootPointer)
