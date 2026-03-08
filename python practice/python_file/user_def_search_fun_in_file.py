

def check_for_fun():
    word="learning"
    with open("practice.txt","r") as f:
         data=f.read()
    if word in data:

        print("found")
    else:
         print("not found")

check_for_fun()
