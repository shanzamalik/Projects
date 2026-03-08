class Person:
    #private variable/attribute
    __name="anonymous"

    def __welcome_in_class(self):
        print("Welcome in class..") 
    
    def welcome_msg(self):
        print("hi buddy..")
        #private method is only access in class/method
        self.__welcome_in_class()

person1=Person()
person1.welcome_msg()
#no private method or variable can be access outside class