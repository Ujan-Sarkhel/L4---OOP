class myCLass:
    def __init__(self, text):
        self.text=text
    def rev(self):
        word=self.text.strip().split()
        rev_word=word[::-1]
        return ' '.join(rev_word)
ob=myCLass("I am Ujan")
print(ob.rev())