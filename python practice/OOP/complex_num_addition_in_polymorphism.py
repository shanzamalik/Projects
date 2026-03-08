class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    #dunder function for adding two complex nums
    def __add__(self,num2):
        newReal=self.real+num2.real 
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
  #dunder function for subtraction of two complex nums
    def __sub__(self,num2):
        newReal=self.real-num2.real 
        newImg=self.img-num2.img
        return Complex(newReal,newImg)   
    
    def show_number(self):
        print(self.real,"i + ",self.img,"j")

num1=Complex(1,3)
num1.show_number()

num2=Complex(4,6)
num2.show_number()

#by defining dunder function,i can add two complex nums
num3=num1+num2
num3.show_number()

#by defining dunder function,i can sub two complex nums
num3=num1-num2
num3.show_number()







     
    