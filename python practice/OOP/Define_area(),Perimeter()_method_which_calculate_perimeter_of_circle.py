class Circle:

    def __init__(self,radius):
        self.radius=radius
    
    def area_of_circle(self):
        return (22/7) * self.radius ** 2

    
    def perimeter_of_circle(self):
        return 2 * (22/7) * self.radius
    
peri=Circle(21)
print("Area of circle:", peri.area_of_circle())
print("Parimeter of circle:", peri.perimeter_of_circle())

#print("Perimeter of circle:",)

    

