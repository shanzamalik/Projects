class A:
    varA="welcome in class A"

class B:
    varB="welcome in class B"

class C(A,B):
    varC="welcome in class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)