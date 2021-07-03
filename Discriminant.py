print("Genral Form:- ax**2 + bx + c = 0")
a = int(input("Enter a: ")) 
if a<0:
    print("Invalid Value(a!=0): ")
    exit()

b = int(input('Enter b: '))  
c = int(input('Enter c: '))  
# To Find Discriminant
d = (b**2) - (4*a*c)
if d<0:
    print ("Unable to reach the root")
    exit()
else:
    print(d)
    