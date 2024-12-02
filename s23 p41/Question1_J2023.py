DataArray = [] # DECLARE DataArray : ARRAY[0:24] OF INTEGER
try:
    file = open("Data.txt", 'r')
    line = file.readline().strip()
    while len(line)>0:
        DataArray.append(int(line))
        line = file.readline().strip()
    file.close()
except FileNotFoundError:
    print("File not found")

#print(DataArray)

def PrintArray(arr):
    for e in arr:
        print(e, end=" ")

#PrintArray(DataArray)

def LinearSearch(arr, find):
    c = 0
    for i in range(len(arr)):
        if arr[i] == find:
            c += 1
    return c

response = int(input("Enter a number: "))
while response < 0 and response > 100:
    response = int(input("Number must be between 0 and 100: "))

print(f"The number {response} was found {LinearSearch(DataArray, response)} times.")
