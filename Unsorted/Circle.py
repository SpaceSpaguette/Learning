import math
def O(z):
    y = (z+1) * math.pi*2

    return y 


def S(R):
 return math.pi * (R**2)


x=0.01
for e in range(30-1):
    x = x*2
    print(x)
if x > 1000000:
    print("jeej milion")
    print(x-1000000)
else:
    print("zadnej milion")
    print(1000000-x)
