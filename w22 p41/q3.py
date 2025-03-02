ArrayNodes = [[1, 20, 5], [2,15,-1], [-1,3,3], [-1,9,4], [-1,10,-1], [-1,58,-1], [-1,-1,-1]]
FreeNode = 6
RootPointer = 0

def SearchValue(Root, ValueToFind):
    global ArrayNodes

    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1] == -1:
                return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)

def PostOrder(root):
    global ArrayNodes
    if(ArrayNodes[root][0] != -1):
        PostOrder(ArrayNodes[root][0])
    if (ArrayNodes[root][2] != -1):
        PostOrder(ArrayNodes[root][2])
    print(ArrayNodes[root][1])

if SearchValue(RootPointer, 15) == -1:
    print("Not found")
else:
    print(f"Found at {SearchValue(RootPointer, 15)}")

PostOrder(RootPointer)


