class Car:
     
    def __init__(self,car_type):
        self.car_type=car_type
   
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def end():
        print("car stopped...")

class ToyotaCar(Car):

     def __init__(self,name,type):
         #if we use super()fun in child class then we can 
        # access the parent class attributes and methods

        super().__init__(type)
        self.name=name
        #we can access class method in child class 
        # through super() constructor
        super().start()
        
    
car1=ToyotaCar("prius","electric")
print(car1.name)
print(car1.car_type)
