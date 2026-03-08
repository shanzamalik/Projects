num=int(input("Enter a num:"))
sum=0
a=num
b=num-1
def cal_sum(num):
    if(num==0):
        return 0
    return num+cal_sum(num-1)#5+4=9+3=12+2=14+1=15
print(cal_sum(num))    
