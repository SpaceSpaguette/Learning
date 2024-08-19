
#this one calculates how many blocks are currently to be mined
#TODO translate to English and use int instead of str

pocet = [input("x "), input("y "), input("z "), input("diamond ")]
celkem = int(pocet[0]) * int(pocet[1]) * int(pocet[2])

print("celkem jsi vytezil " + str(celkem) + " number")

procento = (float(pocet[3]) / celkem) * 100
print(f"{pocet[3]} je {procento:.2f}% z {celkem:.2f}bloku")
