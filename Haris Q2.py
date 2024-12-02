NumberArray = [100, 85, 644, 22, 15, 8, 1]

def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements-1)
        LastItem =  IntegerArray[NumberElements-1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem:
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

recursive_sorted = RecursiveInsertion(NumberArray, len(NumberArray))
print("Recursive")
'''for e in recursive_sorted:
    print(e)'''
print(recursive_sorted)
def IterativeInsertion(IntegerArray, NumberElements):
    for i in range(NumberElements):
        while i >= 0:
            LastItem = IntegerArray[i]
            CheckItem = i - 1
            LoopAgain = True
            #print(f"Last item {LastItem} CheckItem {CheckItem}")
            if CheckItem < 0:
                LoopAgain = False
            elif IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
            while LoopAgain:
                IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
                CheckItem -= 1
                if CheckItem < 0:
                    LoopAgain = False
                elif IntegerArray[CheckItem] < LastItem:
                        LoopAgain = False
            IntegerArray[CheckItem + 1] = LastItem
            #print(IntegerArray)
            i -= 1
    return IntegerArray

iterative_sorted = IterativeInsertion(NumberArray, len(NumberArray))
print("Iterative")
print(iterative_sorted)

'''for e in iterative_sorted:
    print(e)
'''

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    else:
        mid = (First+Last)//2
        if IntegerArray[mid] == ToFind:
            return mid
        elif IntegerArray[mid] > ToFind:
            return BinarySearch(IntegerArray, First, mid-1, ToFind)
        else:
            return BinarySearch(IntegerArray, mid+1, Last, ToFind)

place = BinarySearch(iterative_sorted, 0, len(iterative_sorted)-1, 644)
if place == -1:
    print("Not found")
else:
    print(place)
