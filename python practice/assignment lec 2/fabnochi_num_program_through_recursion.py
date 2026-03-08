f0=0
f1=1

def fabnochi(num):
    if(num==0 or num==1):
        return num
       # num1=f1-1 #4
       # num2=num-2 #3
       # fabnochi(num)#f(4)
        #fabnochi(num)#f(3)
    return fabnochi(num-1)+fabnochi(num-2) #4+3
        #f2=f1+f0
        #f(2)=f(1)+f(0),
        # f(3)=f(2)+f(1),
        #f(4)=f(3)+f(2)
        # f(n)=f(n-1)+f(n-2)
        #return fabnochi(sum_of_nums) #f(3)+f(4)=f(5)
# for i in range(0,10):
#     print (fabnochi(i))
#print (fabnochi(8))

num=int(input("enter a num:"))#8,13
num1=num-1#7,6,12
num2=num-2#6,5,11
print("num1:",num1)
print("num2:",num2)

for i in range(0,num+1):
    num1-=1#6,11,
    num2-=2#5,10
    val1=num1+num2#7+6=13,21
    print(val1)#13,21
    num-=1
    print("value of num:",num)
   

   # val2=num#8
    #sum=val1+val2
  #  print("sum of val1 and val2:",sum)
   


    
   
    
    print("num1 in loop:",num1)
    print("num2 in loop:",num2)
    
    # if num==0 or num==1:
    #      print(num)
    #      if num==1:
    #          print(num)
    
        #print(value of i:)
      
        
       # for sum in range(0,num+1):
           # sum=num1+num2
          
        
    


