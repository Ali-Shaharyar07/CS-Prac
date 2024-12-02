QueueArray = [0 for i in range(10)] #DECLARE QueueArray : ARRAY[0:9] OF STRING
HeadPointer = 0 #DECLARE HeadPointer : INTEGER                            Head points towards first element
TailPointer = 0 #DECLARE TailPointer : INTEGER                            Tail points towards free element
NumItems = 0 #DECLARE NumItems : INTEGER

def Enqueue( DataToAdd):
    global QueueArray, HeadPointer, TailPointer, NumItems
    if NumItems == 10:
        return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumItems += 1
    #print(NumItems)
    return True

def Dequeue():
    global QueueArray, HeadPointer, TailPointer, NumItems
    if NumItems == 0:
        #print(NumItems)
        return False
    if HeadPointer == 9:
        HeadPointer = 0
        NumItems -= 1
        return QueueArray[9]
    else:
        HeadPointer += 1
        NumItems -= 1
        return QueueArray[HeadPointer-1]

for i in range(11):
    response = input(f"Enter string #{i+1}: ")
    status = Enqueue(response)
    if status == False:
        print("Item not added")
    else:
        print("Item Added")
print(Dequeue())
print(Dequeue())