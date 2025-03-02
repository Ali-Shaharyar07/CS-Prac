from array import array


class TreasureChest:
    def __init__(self, q, a, p):
        self.__question = q #DECLARE PRIVATE question : STRING
        self.__answer = a #DECLARE PRIVATE answer : INTEGER
        self.__points = p #DECLARE PRIVATE points: INTEGER

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, ans):
        if ans == self.__answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points//2
        elif attempts == 3 or attempts == 4:
            return self.__points//4
        else:
            return 0

def readData():
   global arrayTreasure
   arrayTreasure = []
   try:
       file = open("TreasureChestData.txt", 'r')
       lines = file.readline().strip()
       count = 0
       while len(lines)>0:
           if count == 0:
               question = lines
               count += 1
           elif count == 1:
               ans = lines
               count += 1
           elif count == 2:
               points = lines
               arrayTreasure.append(TreasureChest(question, int(ans), int(points)))
               count = 0
           lines = file.readline().strip()
       file.close()
   except FileNotFoundError:
       print("File not found")

readData()
question = int(input("Enter a question b/w 1 and 5: "))
while (question > 5 or question < 1): question = int(input("Enter a question b/w 1 and 5: "))

attempts = 1
print(arrayTreasure[question-1].getQuestion())
ans = int(input("Enter answer: "))

while not(arrayTreasure[question-1].checkAnswer(ans)):
    attempts += 1
    ans = int(input("Wrong, Enter answer: "))

print(arrayTreasure[question-1].getPoints(attempts))



