'''
Created on 2016. 10. 25.

@author: kitcoop
'''
class Car:
    handle = 0
    speed = 0
    def __init__(self, name, speed):
        self.speed =speed
        self.name = name
    def showData(self):
        km = '킬로미터'
        msg = '속도:' + str(self.speed) + km
        return msg
    
print(Car.handle, Car.speed)

print()
car1 = Car('tom', 10)
print(car1.handle,car1.name, car1.speed)

car2 = Car('john',20)
print(car2.handle,car2.name, car2.speed)
#print(car2.color)
print(id(Car),id(car1),id(car2)) #원형 클래스는 static 에잇고, 나머지는 heap 에 확보

print()
print(car1.showData())
print(car2.showData())
car1.handle = 20
Car.handle = 30 #프로토타입 바꾸는거
print(car1.handle)
print(car2.handle)
