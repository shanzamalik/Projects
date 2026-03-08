subject={}
subject_1=int(input("Enter a first subject marks:" ))
subject.update({"phy":subject_1})
subject_2=int(input("Enter a second subject marks:" ))
subject.update({"chem":subject_2})
subject_3=int(input("Enter a third subject marks:" ))
subject.update({"eng":subject_3})

print(subject.items())

