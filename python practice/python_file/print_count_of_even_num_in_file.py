with open("problem.txt","r") as f:
  count=0
  data=f.read()
  num=data.split(",")#num is a list here
for val in num:
  if (int(val)%2==0):
    print("value:",val)
    print("value of num:",num)
    count+=1
  print("value outside that not in mod loop:",val)
print("even num count:",count)

     

      
   
  
 
