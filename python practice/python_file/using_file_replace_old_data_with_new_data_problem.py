with open("practice.txt","r") as f:
    data=f.read()
    #in strings,we can replace data using replace fun
    new_data=data.replace("Java","Python") 
    print(new_data)
    
with open("practice.txt","w") as f:
    f.write(new_data)
 