class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    def calc_percentage(self):
        self.percentage=str((self.phy+self.chem+self.math)/3) + "%"
        print("inside fun value of %:",self.percentage)

stu1=Student(98,97,99)
print(stu1.phy)

stu1.calc_percentage()
print(stu1.percentage)
