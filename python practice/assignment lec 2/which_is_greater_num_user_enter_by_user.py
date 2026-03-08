num1=int(input("enter a first number: "))
num2=int(input("enter a second number: "))
num3=int(input("enter a third number: "))
if(num1>=num2 and num1>=num3):
    print(num1,"is a greater")
elif(num2>num3):
     print(num2,"is a greater")
else:
     print(num3,"is a greater")