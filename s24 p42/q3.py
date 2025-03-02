
NumberArray = [100, 85, 644, 22, 15, 8, 1]

def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements-1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    while LoopAgain:
        IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False

    IntegerArray[CheckItem+1] = LastItem
    return IntegerArray

#rI = RecursiveInsertion(NumberArray, len(NumberArray))
#print("Recursive: ", rI)

#NumberArray = [100, 85, 644, 22, 15, 8, 1]

def IterativeInsertion(IntegerArray, NumberElements):
    for i in range(1, NumberElements):
        key = IntegerArray[i]
        place = i-1
        while place >= 0 and IntegerArray[place] > key:
            IntegerArray[place+1] = IntegerArray[place]
            place -= 1
        IntegerArray[place+1] = key
    return IntegerArray


iI = IterativeInsertion(NumberArray, len(NumberArray))
print("Iterative: ", iI)

def BinarySearch(IntegerArray, First, Last, ToFind):

    if First > Last:
        return -1
    else:
        mid = (First + Last) // 2
        if (IntegerArray[mid] == ToFind):
            return mid
        elif (IntegerArray[mid] < ToFind):
            return BinarySearch(IntegerArray, mid+1, Last, ToFind)
        else:
            return BinarySearch(IntegerArray, First, mid-1, ToFind)

print(BinarySearch(NumberArray, 0, 6, 644))


