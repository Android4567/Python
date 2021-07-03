import math
A = int(input("Enter the First Value "))
B = int(input("Enter the Second Value "))
C = int(input("Enter the Third Value "))
S = (A + B + C) / 2
area = math.sqrt(S * (S - A) * (S - B) * (S - C))
print(area)