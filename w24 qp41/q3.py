LinkedList = [[-1, i+1] for i in range(20)]
LinkedList[19][1] = -1
FirstEmpty = 0
FirstNode = -1

def InsertData():
    global LinkedList, FirstNode, FirstEmpty
    for i in range(5):
        insertData = int(input("Enter data: "))
        if FirstEmpty != -1:
            NextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = insertData
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = NextEmpty

def OutputLinkedList():
    global LinkedList, FirstNode
    currentNode = FirstNode
    while currentNode != -1:
        print(LinkedList[currentNode][0])
        currentNode = LinkedList[currentNode][1]

def RemoveData(remove):
    global LinkedList, FirstNode, FirstEmpty
    currentNode = FirstNode
    previousNode = 0
    while currentNode != -1 and LinkedList[currentNode][0] != remove:
        previousNode = currentNode
        currentNode = LinkedList[currentNode][1]

    if currentNode == FirstNode:
        FirstNode = LinkedList[FirstNode][1]
    else:
        LinkedList[previousNode][1] = LinkedList[currentNode][1]
    LinkedList[currentNode][0] = -1
    LinkedList[currentNode][1] = FirstEmpty
    FirstEmpty = currentNode





InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()