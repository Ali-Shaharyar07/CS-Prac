from numbers import Number


class Node:
    def __init__(self, d):
        self.__LeftPointer = -1 #DECLARE PRIVATE LeftPointer : INTEGER
        self.__Data = d #DECLARE PRIVATE Data : INTEGER
        self.__RightPointer = -1 #DECLARE PRIVATE RightPointer : INTEGER

    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data

    def SetLeft(self, l):
        self.__LeftPointer = l
    def SetRight(self, r):
        self.__RightPointer = r
    def SetData(self, d):
        self.__Data = d

class TreeClass:
    def __init__(self):
        self.__Tree = [Node(-1) for i in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0

    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes].SetData(NewNode)
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes].SetData(NewNode)
            currentP = self.__FirstNode
            prevP = 0
            isLeft = False
            while currentP != -1:
                prevP = currentP
                if NewNode < self.__Tree[currentP].GetData():
                    currentP = self.__Tree[currentP].GetLeft()
                    isLeft = True

                elif NewNode > self.__Tree[currentP].GetData():
                    currentP = self.__Tree[currentP].GetRight()
                    isLeft = False

            if isLeft:
                self.__Tree[prevP].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[prevP].SetRight(self.__NumberNodes)
            self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for i in range(0, self.__NumberNodes):
                print(self.__Tree[i].GetLeft(), " ", self.__Tree[i].GetData(), " ", self.__Tree[i].GetRight())

TheTree = TreeClass()

TheTree.InsertNode(10)
TheTree.InsertNode(11)
TheTree.InsertNode(5)
TheTree.InsertNode(1)
TheTree.InsertNode(20)
TheTree.InsertNode(7)
TheTree.InsertNode(15)

TheTree.OutputTree()