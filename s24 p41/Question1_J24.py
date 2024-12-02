#DECLARE NumberItems : INTEGER
#DECLARE DataStored : ARRAY[0:19] OF INTEGER

global NumberItems
global DataStored
DataStored = []

def Initialise():
    global NumberItems
    global DataStored

    NumberItems = int(input("Enter amount of numbers to enter: "))
    while (NumberItems<1 or NumberItems>20):
        NumberItems = int(input("Number must be between 1 and 20: "))
    for i in range(NumberItems):
        DataStored.append(int(input(f"Enter number #{i+1}: ")))
NumberItems = 0
Initialise()
#print(DataStored)

def BubbleSort():
    ncompare = NumberItems-1
    swap = False
    while (not swap and ncompare>=0):
        for i in range(ncompare):
            if (DataStored[i] > DataStored[i+1]):
                temp = DataStored[i+1]
                DataStored[i+1] = DataStored[i]
                DataStored[i] = temp
        ncompare -= 1

BubbleSort()
#print(DataStored)

def BinarySearch(DataToFind):
    global NumberItems
    global DataStored
    first = 0
    last = NumberItems-1

    while (last >= first):
        mid = (first + last)//2
        #print(f"last {last} + first {first} + mid{mid}")
        if (DataStored[mid] == DataToFind):
            return mid
        elif (DataStored[mid] > DataToFind):
            last = mid-1
        elif (DataStored[mid] < DataToFind):
            first = mid+1
    return -1

n = int(input("Enter a number: "))
print(BinarySearch(n))

