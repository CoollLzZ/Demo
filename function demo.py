print("Hollow star generator\n\n")

star = int(input("How many stars u want? "))

for i in range(0, star):
    print("*", end="    ")
    
print("\n")

for i in range(0, star-2):
    
    for i in range(0, star):
        if i == 0 or i == star-1:
            print("*", end ="    ")
        else:
            print(" ", end ="    ")
            
    print("\n")
    
for i in range(0, star):
    print("*", end="    ")
