TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(TheData):
    for count in range(0, len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue>=0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue+1] = TheData[NextValue]
                NextValue -= 1
                TheData[NextValue+1] = DataToInsert
            else:
                Inserted = 1

def PrintArray(TheData):
    for i in range(len(TheData)):
        print(TheData[i])

'''print("Before sorting")
PrintArray(TheData)
InsertionSort(TheData)
print("After sorting")
PrintArray(TheData)'''

def Search():
    global TheData
    find = int(input("Enter number to find: "))
    for e in TheData:
        if e == find:
            print("Found")
            return True
    print("Not Found")
    return False

Search()


