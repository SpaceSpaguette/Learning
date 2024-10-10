class celecislo:
    def __init__ (self):
        self.number= []

    def je_prirozene(self,cele_cislo):
        self.number = cele_cislo
        for x in range(len(cele_cislo)):
            if self.number[x] <0:
                self.number[x] = False
            else:
                self.number[x] = True
    def __str__ (self):
        return str(self.number)
x1 = celecislo()
x1.je_prirozene([1,2,4,5,-1,2,5,-2,-2,3-4,5,-5])
print(x1)
r1 = 0
r2 = 0
for x in x1.number:
    if x is not None and x:
        r1 += 1
    else:
        r2 += 1
print(r1, r2)