import random

cour = 0
sum = 13
NumC = 4
val = [0, 0, 0, 0]
tries = 0
check = []
num_cz =0
cannot = []




for x in range(2):
    for y in range(5):
        for z in range(10):
            for f in range(10):
                val[0],val[1],val[2],val[3] = x,y,z,f
                
                num_cz+=1
                if val[0]+val[1]+val[2]+val[3] == 13 and val[0]<val[1]<val[2]<val[3]:
                    print(val)
                    NumC+=1


print(NumC)
print(num_cz)
