class node:
    def __init__(self, d, n):
        self.data = d #DECLARE data : INTEGER
        self.nextNode = n #DECLARE nextNode : INTEGER

global linkedList, startPointer, emptyList

linkedList = [node(1, 1), node(5, 4), node(6,7), node(7, -1), node(2, 2),
              node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]

startPointer = 0
emptyList = 5

def outputNodes(currentPointer):
    global linkedList
    while currentPointer != -1:
        print(linkedList[currentPointer].data)
        currentPointer = linkedList[currentPointer].nextNode

def addNode(currentP):
    global linkedList, startPointer, emptyList
    freeP = emptyList

    if freeP < 0 or freeP > 9:
        return False
    else:
        data = int(input("Enter data: "))
        newNode = node(data, -1)
        linkedList[freeP] = newNode
        emptyList = linkedList[emptyList].nextNode

        prevP = 0
        while currentP != -1:
            prevP = currentP
            currentP = linkedList[currentP].nextNode
        linkedList[prevP].nextNode = freeP
        return True

outputNodes(startPointer)
result = addNode(startPointer)
if result:
    print("Success")
else:
    print("LL is full")
outputNodes(startPointer)