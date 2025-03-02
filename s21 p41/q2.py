from PIL.GimpGradientFile import linear

global arrayData
arrayData = [10, 5, 6, 7, 1 ,12, 13, 15, 21, 8]

def linearSearch(num):
    global arrayData
    for i in range(0, len(arrayData)):
        if arrayData[i] == num:
            return True
    return False

'''val = int(input("Enter a value: "))
if linearSearch(val):
    print("Found")
else:
    print("Not found")'''

def bubbleSort():
    global arrayData
    temp = 0
    for x in range(0, len(arrayData)):
        for y in range(0, len(arrayData)-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
bubbleSort()
print(arrayData)

