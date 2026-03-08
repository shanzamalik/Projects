class Person:
    name="anonymous"
    def change_name(self,name):
       # self obj hota hai.
       #jis class k attribute ko change krna es method
      # sa us class ko access krty
      #eg obj(self).__class__.name(attribute)
       self.__class__.name="aizal"
       #we can access the class in fun to:
       


p1=Person()
p1.change_name("zarwa")
#print(p1.name)
#print(Person.name)
print(p1.name)
print(Person.name)