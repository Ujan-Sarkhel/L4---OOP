class Pri:
    __privateVar = 2

    def __privMeth():
        print("i am ujan")
    def hello():
        print(Pri.__privateVar)

ob=Pri()
ob.__privMeth()
ob.hello()