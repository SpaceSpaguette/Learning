'''what we know. is that last number of any 

'''
#Simple values
inter = 0

#The bruteforce attack.
for x in range(2):
  for y in range(4):
    for z in range(6):
      for a in range(9):
        inter += 1
        if x < y < z < a:
          if x+y+z+a == 13:
            print(f"{x}{y}{z}{a}", end=" ")
print(f"total iteracions:{inter}")

