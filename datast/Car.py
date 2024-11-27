class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def display(self):
        print(self.color, ":", self.speed)

    def isEqual(self, carB):
        if self.color == carB.color:
            return True
        else:
            return False

    def __eq__(self,carB):
        return self.color == carB.color

    def __str__(self):
        return "color = %s, speed = %d" %(self.color, self.speed)



if __name__ == "__main__":
    car1 = Car("black", 0)
    car2 = Car("red", 130)
    car3 = Car("yellow")
    car5 = Car("black", 10)
    car4 = Car("red", 110)

    car1.speedUp()
    car2.speedDown()
    car1.display()
    car2.display()
    car3.display()
    car5.display()
    car4.display()
    print(car1.isEqual(car3))
    print(car2.isEqual(car4))
    print(car1 == car4)
    print(car2 == car4)
    print(car3)