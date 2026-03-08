class Person:
    name="anonymous"
    @classmethod
    def change_name(cls,name):
       # cls(class) obj hota hai.
       #jis class k attribute ko change krna es method
      # sa us class ko access krty
      #eg cls.__class__.name(attribute)
       cls.name="aizal"
       #we can access the class in fun to:
       


p1=Person()
p1.change_name("zarwa")
#print(p1.name)
#print(Person.name)
print(p1.name)
print(Person.name)