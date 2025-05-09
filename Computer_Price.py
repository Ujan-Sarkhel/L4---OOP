class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling price is", self.__maxprice)
    def setPrice(self, price):
        self.__maxprice=price
ob=Computer()
ob.sell()

ob.setPrice(1000)
ob.sell()