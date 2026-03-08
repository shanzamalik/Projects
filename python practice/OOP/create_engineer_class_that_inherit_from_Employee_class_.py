class Employee:
    def __init__(self,p_role,p_depart,p_salary):
        self.role=p_role
        self.department=p_depart
        self.salary=p_salary
    
   
    def showDetails_ofemployee(self):
        print("Employee role:",self.role)
        print("Employee department:",self.department)
        print("Employee salary:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        
        self.name=name
        self.age=age
        print("Employee name:",self.name)
        print("Employee age:",self.age)
        super().__init__("Engineer","IT","75,000")
    
     

employee1=Engineer("Elon Musk","40")
employee1.showDetails_ofemployee()

