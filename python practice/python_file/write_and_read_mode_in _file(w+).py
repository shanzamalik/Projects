f=open("sample.txt","w+")
#w+ truncate all data from file,and show empty file
#if we read, we can use then write
#  function to write in data again
f.read()
print(f.read())
f.write("abc")
f.close()