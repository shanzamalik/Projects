class Car:
    #base class/parent class
   
    color="blue"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def end():
        print("car stopped...")
class ToyotaCar(Car):
     #child class/derived class..
    #car class is inherited here..

     def __init__(self,name):
        self.name=name
        print("obj created:")
        print("constructor of toyota class")
      


car1=ToyotaCar("prius")
car2=ToyotaCar("Fortuner")
car1.start()
print("car 1 color:",car1.color)
print("car 2 color:",car2.color)