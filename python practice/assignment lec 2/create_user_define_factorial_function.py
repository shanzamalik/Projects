

def fact_fun(num):
    print("value of num:",num)
    fact=1

    for i in range(1,num+1):
        fact*=i
    print("fact of num:" ,fact)


fact_fun(6)