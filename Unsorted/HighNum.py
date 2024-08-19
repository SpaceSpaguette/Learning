print("it begins here")
number = int(input("Enter a number"))

numberrow = []
for x in range(4):
    numberrow.append(number+x*10)
print(numberrow)
numberrow.sort()

#takes the totaly highest number and outputs it to the screen
print(numberrow[-1])



