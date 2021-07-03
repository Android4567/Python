'''
# The number is Armstrong or Not

def Armstrong_Or_Not(num):
    
    val = 0
    for i in num:
        val = val+int(i)**3
    if str(val) == num:
        print("Amstrong number")
    else:
        print("not a Amstrong")
    
Armstrong_Or_Not( num = input("Enter a value => "))

# Armstrong numbers of Three Numbers

firstval = int(input("Enter a first value => "))
secondval = int(input("Enter The Second Value => "))
for num in range(firstval,secondval+1):
    val = 0
    num = str(num)
    for i in num:
        val = val+int(i)**3
    if str(val) == num:
        print(f"{val} Amstrong number")


# Armstrong numbers of Four Numbers

firstval = int(input("Enter a first value => "))
secondval = int(input("Enter The Second Value => "))
for num in range(firstval,secondval+1):
    val = 0
    num = str(num)
    for i in num:
        val = val+int(i)**4
    if str(val) == num:
        print(f"{val} Amstrong number")
'''
