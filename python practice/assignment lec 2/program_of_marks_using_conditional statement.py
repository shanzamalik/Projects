marks=float(input("enter a marks: "))
if(marks>=90):
    marks="A"
elif(marks<90 and marks>=80):
     marks="B"
elif(marks<80 and marks>=70):
     marks="C"
else:
    marks="D"
print("grade of student: " ,marks)