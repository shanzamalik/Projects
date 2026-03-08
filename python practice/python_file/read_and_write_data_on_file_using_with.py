with open("sample.txt","r") as f:
    #with syntax close the function no need to write
    data=f.read()
    print(data)

with open("sample.txt","w")as f:
    data=f.write("new data")
  

