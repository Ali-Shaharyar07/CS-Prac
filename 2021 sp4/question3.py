from queue import Queue

QueueData = [] #DECLARE QueueData : ARRAY[0:19] OF STRING
StartPointer = -1 #DECLARE StartPointer : INTEGER
EndPointer = -1 #DECLARE EndPointer : INTEGER

def Enqueue(item):
    global EndPointer
    global StartPointer
    global QueueData

    if EndPointer == 19:
        return False
    elif EndPointer == -1:
        StartPointer = 0

    EndPointer += 1
    QueueData.append(item)
    return True

def ReadFile():
    name = input("Enter file name: ")
    try:
        file = open(name, 'r')
        line = file.readline().strip()
        full = False
        while len(line) > 0:
            full = Enqueue(line)
            if not full:
                return 1
            line = file.readline().strip()
        file.close()
        return 2
    except FileNotFoundError:
        return -1

status = ReadFile()

if status == -1:
    print("File not Found")
elif status == 1:
    print("Queue is full")
else:
    print("All items added")

def Remove():
    global QueueData
    global StartPointer
    global EndPointer
    ans = ""
    if EndPointer - StartPointer < 1: # minimum must be sp = 0, ep = 1 -> ep-sp = 1 hence must always be less < 1 for no items
        ans = "No items"
    else:
        ans = QueueData[StartPointer] + " " + QueueData[StartPointer+1]
    return ans

print(Remove())


