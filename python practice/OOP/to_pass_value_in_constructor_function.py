class Student:
    collage_name="ABC college"#(class attribute)
#default constructor
    def __init__(self):
        pass

   #parameter constructor
    def __init__(self,name,marks):
        self.name=name#we create name variable 
        #that assign s1 value to name.
        self.marks=marks#(object attribbute)
        print("Add student value in database:")
#these are functions in class we call it methods
    def welcome(self):
        print("welcome in class:",self.name)
    def getmarks(self):
        print(self.marks)

s1=Student("shanza",'90')
print(s1.name,s1.marks)

s2=Student("zarwa",'70')
print(s2.name,s2.marks)

s1.welcome()
s1.getmarks()