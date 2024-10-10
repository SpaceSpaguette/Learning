class sort:
    def __init__(self):
        self.num = []
        self.meth = "vzestupne"
    
    def serad(self,numbers,meth = "sestupne"):
        self.num = numbers
        if meth == "vzestupne":
            self.num.sort()
        if meth == "sestupne":
            self.num.sort(reverse = True)
    def __str__(self):
        return str(self.num)

x = sort()
x.serad([5, 3, 7, 1, 9, 4, 2, 8, 6], "sestupne")
print(x)