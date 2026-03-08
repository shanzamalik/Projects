f=open("sample.txt","a+")
#append and read mode ,
#it append the data with already file

print(f.read())
f.write("abc")

f.close()