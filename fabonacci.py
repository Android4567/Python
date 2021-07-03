firstvalue = 0
secondvalue = 1
num = int(input("Enter a number => "))
if num <= 0:
    print("not possible")
elif num == 1:
    print(firstvalue)
else:
    print(firstvalue)
    print(secondvalue)
    for i in range(2,num):
        thirdvalue = firstvalue + secondvalue
        print(thirdvalue)
        firstvalue = secondvalue
        secondvalue = thirdvalue
