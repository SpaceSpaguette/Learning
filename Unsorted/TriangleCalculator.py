


#calculates square triangle
def triangle_3(h):
    for i in range(1, h+1):
        print(" "*(h - i), end="")
    for j in range(0,i):
        print("000 ", end="")
        print()
    
triangle_3(5)