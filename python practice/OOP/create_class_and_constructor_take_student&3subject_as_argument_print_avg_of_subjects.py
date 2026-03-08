class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.mark=marks
    
        print("student name and marks:")
    
    def get_average(self,marks):
        sum=0
        for val in marks:
            sum+=val
        print("hi ",self.name," your average marks :",sum/3)
        #method 2:
        #avg=sum(marks)/len(marks)
        #print("average of nums:",avg)

student1=Student("zarwa",[99,98,97])
student1.get_average([99,98,97])

student1.name="shanza"
student1.get_average([20,30,40])




