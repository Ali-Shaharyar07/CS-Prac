from os import remove


class SaleData:
    def __init__(self, id, quan):
        self.ID = id
        self.quantity = quan

global CircularQueue, Head, Tail, NumberOfItems

CircularQueue = [SaleData("", -1) for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(item):
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems >= 5:
        return -1
    else:
        CircularQueue[Tail] = item
        Tail += 1
        if Tail>4: Tail = 0
        NumberOfItems += 1
        return 1

def Dequeue():
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems == 0:
        return SaleData("", -1)
    else:
        NumberOfItems -= 1
        removed = CircularQueue[Head]
        if Head == 4: Head = 0
        else: Head += 1
        return removed

def EnterRecord():
    id = input("Enter an ID: ")
    quant = int(input("Enter the quantity: "))
    record = SaleData(id, quant)
    if Enqueue(record) == 1:
        print("Stored")
    else:
        print("Full")

EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
removedRecord = Dequeue()
if removedRecord.ID == "":
    print("Error, Queue is empty")
else:
    print(removedRecord.ID, " ", removedRecord.quantity)
EnterRecord()

for e in CircularQueue:
    print(e.ID, " ", e.quantity)