global QueueData #DECLARE QueueData : ARRAY[0:19]
global QueueHead #DECLARE QueueHead : INTEGER
global QueueTail #DECLARE QueueTail : INTEGER

QueueData = [ "" for i in range(20)]
QueueHead = -1
QueueTail = -1
#print(QueueData)
def Enqueue(insert):
    global QueueData
    global QueueHead
    global QueueTail

    if QueueTail == 19:
        return False
    elif QueueHead == -1:
        QueueHead = 0

    QueueTail += 1
    #print(QueueTail)
    QueueData[QueueTail] = insert
    return True

def Dequeue():
    global QueueData
    global QueueHead
    global QueueTail

    if QueueHead < 0 or QueueHead > QueueTail :
        return "False"
    else:
        QueueHead += 1
        return QueueData[QueueHead-1]

def StoreItems():
    responses = []
    c = 0
    for i in range(10):
        chars = []
        responses.append(input(f"Enter string #{i+1}: "))
        for e in responses[i]:
            chars.append(e)
        total = int(chars[0]) + int(chars[2]) + int(chars[4]) + (int(chars[1])*3) + (int(chars[3])*3) + (int(chars[5])*3)
        checkDigit = total//10
        #print(f"checkdigit: {checkDigit}")
        if checkDigit == 10 and chars[6] == 'X':
            responses[i] = chars[0] + chars[1] + chars[2] + chars[3] + chars[4] + chars[5]
            if Enqueue(responses[i]):
                print("Inserted item ")
            else:
                print("Queue is full")
        elif checkDigit == int(chars[6]):
            responses[i] = chars[0]+ chars[1]+ chars[2]+ chars[3]+ chars[4]+ chars[5]
            if Enqueue(responses[i]):
                print("Inserted item ")
            else:
                print("Queue is full")
        else:
            c += 1

    print(f"{c} invalid items")

StoreItems()
x = Dequeue()
if x == "False":
    print("Queue is empty")
else:
    print(x)

