from Car import Car

class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True ):
        super().__init__(color, speed)
        self.bTurbo = bTurbo

    def setTurbo(self, bTurbo = True):
        self.bTurbo = bTurbo

    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()

    def speedDown(self):
        if self.bTurbo:
            self.speed -= 50
        else:
            super().speedUp()

    def __str__(self):
        if self.bTurbo:
            return "[%s] [speed = %s] 터보모드" %(self.color, self.speed)
        else:
            return "[%s] [speed = %s] 일반모드" %(self.color, self.speed)
s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("White",0,False)
s1.speedUp()
s2.speedUp()

print("조현식1:",s1)
print("조현식2:",s2)