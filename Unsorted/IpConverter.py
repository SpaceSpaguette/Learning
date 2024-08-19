ip = "192.168.10.2"
COnverted = []
for x in ip.split("."):
    x=int(x)
    binary_num = ""
    while x > 0:
        remainder = x % 2
        binary_num = str(remainder) + binary_num
        x = x // 2
    COnverted.append(binary_num.rstrip("."))
print(*COnverted, sep=".")
print(".".join(COnverted),end="")