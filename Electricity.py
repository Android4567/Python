Unit = int(input("Input The Number of unit you consumed in a month "))
if Unit < 100:
    print("You have to pay 0 RS ")
    p = Unit * 0
elif Unit >= 100 and Unit <200:
    print("You Have to pay 5 RS per unit")
    p = Unit * 5
elif Unit >= 200 and Unit <300:
    print("You Have to pay 7 RS per unit")
    p = Unit * 7
elif Unit >= 300 and Unit <500:
    print("You Have to pay 9 RS per unit")
    p = Unit * 9
elif Unit >=500:
    print("You Have to pay 10 RS per unit")
    p = Unit * 10
# Discount According to city
city = input("ENTER YOUR CITY:- Delhi,Mumbai,Kolkata,Chennai and Others ")
if city.lower() == "delhi":
    a = (10 / 100 * p)
elif city.lower() == "mumbai":
    a = (7 / 100 * p)
elif city.lower() == "kolkata":
    a = (5 / 100 * p)
elif city.lower() == "chennai":
    a = (2 / 100 * p)
else:
    a = (0 / 100 * p)
ta = (p-a)
print(f"You Have To pay:- {ta} RS ")