f=open("sample.txt","r+")
#r+ means pointer go at the start 
# and overwrite the already written data in a file.
f.write("abc")
print(f.read())#where the pointer reach 
#after overwrite
f.close()