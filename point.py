class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        print("{0},{1}".format(self.x,self.y))
ob=Point(2,3)
ob.__str__()