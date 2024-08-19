celkem = int(([input("x "), input("y "), input("z "), input("diamond ")])[0]) * int(([input("x "), input("y "), input("z "), input("diamond ")])[1]) * int(([input("x "), input("y "), input("z "), input("diamond ")])[2])

print("celkem jsi vytezil " + str(celkem) + " number")

procento = (float(([input("x "), input("y "), input("z "), input("diamond ")])[3]) / celkem) * 100
print(f"{([input("x "), input("y "), input("z "), input("diamond ")])[3]} je {procento:.2f}% z {celkem:.2f}")

