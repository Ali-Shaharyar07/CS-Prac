class Vehicle:
    #DECLARE PRIVATE ID : STRING
    # DECLARE PRIVATE MaxSpeed : INTEGER
    # DECLARE PRIVATE CurrentSpeed : INTEGER
    # DECLARE PRIVATE IncreaseAmount : INTEGER
    # DECLARE PRIVATE HorizontalPosition : INTEGER

    def __init__(self, id, maxS, a):
        self.__ID = id
        self.__MaxSpeed = maxS
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = a
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, s):
        self.__CurrentSpeed = s
    def SetHorizontalPositon(self, h):
        self.__HorizontalPosition = h

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if (self.__CurrentSpeed > self.__MaxSpeed):
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed

    def PrintPos(self):
        print(f"Horizontal Position: {self.__HorizontalPosition}\nCurrent Speed: {self.__CurrentSpeed}")

class Helicopter(Vehicle):
    #DECLARE PRIVATE VerticalPosition : INTEGER
    #DECLARE PRIVATE VerticalChange : INTEGER
    #DECLARE PRIVATE MaxHeight : INTEGER

    def __init__(self, id, maxS, a, vc, maxH):
        Vehicle.__init__(self, id, maxS, a)
        self.__VerticalChange = vc
        self.__MaxHeight = maxH
        self.__VerticalPosition = 0

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        Vehicle.SetCurrentSpeed(self, Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmount(self))
        if Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self):
            Vehicle.SetCurrentSpeed(self, Vehicle.GetMaxSpeed(self))
        Vehicle.SetHorizontalPositon(self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self))

    def PrintPos(self):
        print(f"Horizontal Position: {Vehicle.GetHorizontalPosition(self)}\nCurrent Speed: {Vehicle.GetCurrentSpeed(self)}\nVertical Position: {self.__VerticalPosition}")

car = Vehicle("Tiger", 100, 20)
heli = Helicopter("Lion", 350, 40, 3, 100)
car.IncreaseSpeed()
car.IncreaseSpeed()
car.PrintPos()
heli.IncreaseSpeed()
heli.IncreaseSpeed()
heli.PrintPos()





