Name = input("Enter Student Name ")
English = int(input("Enter The Marks Of English "))
Hindi = int(input("Enter The Marks Of Hindi "))
maths = int(input("Enter The Marks Of Maths "))
Science = int(input("Enter The Marks Of Science "))
SST = int(input("Enter The Marks Of SST "))
TM = English +  Hindi + maths + Science + SST
Percentage = TM / 500 * 100
print(f"Total Marks of {Name} is = {TM}" )
print(f"And the percentage of {Name} is = {Percentage}%")
if Percentage<33:
    print("FAIL")
elif Percentage>=33 and Percentage<40:
    print("Grade = 'D'")
elif Percentage>=40 and Percentage<50:
    print("Grade = 'C2'")
elif Percentage>=50 and Percentage<60:
    print("Grade = 'C1'")
elif Percentage>=60 and Percentage<70:
    print("Grade = 'B2'")
elif Percentage>=70 and Percentage<80:
    print("Grade= 'B1'")
elif Percentage>=80 and Percentage<90:
    print("Grade = 'A2'")
elif Percentage>=90 and Percentage<100:
    print("Grade = 'A1'")
