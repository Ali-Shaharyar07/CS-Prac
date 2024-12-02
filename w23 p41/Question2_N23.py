from logging import LogRecord
from sys import flags
from tokenize import Number

global Queue #DECLARE Queue : ARRAY[0:49] OF STRING
global HeadPointer #DECLARE HeadPointer : INTEGER
global TailPointer #DECLARE TailPointer : INTEGER

Queue = []
HeadPointer = -1 #First element
TailPointer = 0 #Next Available space

def Enqueue(insert):
    global Queue, HeadPointer, TailPointer

    if TailPointer == 50:
        print("Queue is full")
    elif TailPointer == 0:
        HeadPointer = 0
        Queue.append(insert)
        TailPointer += 1
    else:
        Queue.append(insert)
        TailPointer += 1

def Dequeue():
    global Queue, HeadPointer, TailPointer

    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue empty")
        return "Empty"
    else:
        HeadPointer += 1
        #   print(HeadPointer, TailPointer)
        return Queue[HeadPointer-1]

def ReadData():
    global Queue, HeadPointer, TailPointer
    try:
        file = open("QueueData.txt", 'r')
        line = file.readline().strip()

        while len(line) > 0:
            Enqueue(line)
            line = file.readline().strip()
        file.close()
    except FileNotFoundError:
        print("File not found")

class RecordData():
    #DECLARE ID : STRING
    #DECLARE Total : INTEGER

    def __init__(self, id, total):
        self.ID = id
        self.Total = total

global Records #DECLARE Records : ARRAY[0:49] OF RecordData
global NumberRecords

Records = [RecordData("", 0) for i in range(50)]
NumberRecords = 0

def TotalData():
    global Records, NumberRecords
    #DECLARE DataAccessed : STRING
    #DECLARE Flag : BOOLEAN

    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        #print("DataAccessed", DataAccessed)
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total += 1
                Flag = True
    if not Flag:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

def OutputRecords():
    global Records, NumberRecords
    for i in range(NumberRecords):
        print(f"ID {Records[i].ID} Total {Records[i].Total}")

ReadData()
for e in Queue:
    TotalData()
OutputRecords()







