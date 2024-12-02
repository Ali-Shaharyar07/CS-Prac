class Character:
    #DECLARE Name : STRING
    #DECLARE XPosition : INTEGER
    #DECLARE YPosition : INTEGER

    def __init__(self, name, x, y):
        self.Name = name
        self.XPosition = x
        self.YPosition = y

    def GetXPosition(self):
        return self.XPosition
    def GetYPosition(self):
        return self.YPosition

    def SetXPosition(self, x):
        if x > 10000:
            self.XPosition = 10000
        elif x < 0:
            self.XPosition = 0
        else:
            self.XPosition = x
    def SetYPosition(self, y):
        if y > 10000:
            self.YPosition = 10000
        elif y < 0:
            self.YPosition = 0
        else:
            self.YPosition = y

    def Move(self, key):
        if key == "up":
            self.SetYPosition(self.GetYPosition() + 10)
        elif key == "down":
            self.SetYPosition(self.GetYPosition() - 10)
        elif key == "left":
            self.SetXPosition(self.GetXPosition() - 10)
        elif key == "right":
            self.SetXPosition(self.GetXPosition() + 10)

Jack = Character("Jack", 50, 50)

class BikeCharacter(Character):

    def __init__(self, name, x, y):
        Character.__init__(self, name, x, y)

    def Move(self, key):
        if key == "up":
            Character.SetYPosition(self, self.GetYPosition() + 20)
        elif key == "down":
            Character.SetYPosition(self, self.GetYPosition() - 20)
        elif key == "left":
            Character.SetXPosition(self, self.GetXPosition() - 20)
        elif key == "right":
            Character.SetXPosition(self, self.GetXPosition() + 20)

Karla = BikeCharacter("Karla", 100, 50)

char = input("Which of the characters would you like to choose? (Jack/Karla): ")
while not(char == "jack" or char == "karla"):
    char = input("Please choose between Jack and Karla: ")
dir = input("Which direction would you like to move?: ")
while not(dir == "up" or dir == "down" or dir == "left" or dir == "right"):
    dir = input("Please choose between up, down, left or right: ")

if char == "jack":
    Jack.Move(dir)
    print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
elif char == "karla":
    Karla.Move(dir)
    print(f"Karla's new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")