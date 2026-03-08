class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,item2,price2):
        self.item2=item2
        self.price2=price2
        super().__init__(self.item,self.price)
        if(self.price>self.price2):
            print("first order is greater than second")
        else:
            print("first order is not greater")

order1=Order("Burger","200")
order2=Order("tea","100")



    