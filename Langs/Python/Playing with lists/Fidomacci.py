import colorama
#i want it to be colored
colorama.init(autoreset=True)

def fidomacci(n):
    squence = [0,1]
    hold = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for x in range(n):
            if squence[0] >= squence[1]:
                squence[1] += squence[0]
            else:
                squence[0]+=squence[1]
            print(squence)
    print(max(squence))
print(fidomacci(5))