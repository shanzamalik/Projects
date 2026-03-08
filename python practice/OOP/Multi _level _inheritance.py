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
     #child class/derived class of Car class..
    #car class is inherited here..

     def __init__(self,brand):
        self.brand=brand
        print("obj of toyota class created:")
        print("constructor of toyota class call")

class Fortuner(ToyotaCar):
    #Fortuner class is a child class of Toyotacar,
    #as Toyotacar is derived from Car class(parent) so,
    #all the features and methods of Car class and 
    #  Toyota class is inherit in Fortuner class 
    
    def __init__(self,car_type):
        print("obj of fortuner class created:")
        print("constructor of fortuner class call")
        self.car_type=car_type
        print(self.car_type)
        
       

car1=Fortuner("diesel")
car1.start()