# Patient Record
print("        PATIENT RECORD")
name = input("Enter The Patient Name = ")
age = int(input("Enter The Patient Age = "))
if age<=0:
	print("invalid Age")
gender = input("Enter The Patient Gender (male/Female) = ")
illness = input("Enter The Patient Disease = ")
employment = input("Enter The Patient Employment (Govt,Pvt,Student,Others) = ")
admitdays = int(input("Enter The Admitdays  = "))
# Amount according to Admit Days
if admitdays<=0:
	print("Invalid Days")
	exit()
elif admitdays<=5:
	amount = admitdays*500
elif admitdays>5 and admitdays<=10:
	amount = admitdays*400
elif admitdays>10 and admitdays<=30:
	amount = admitdays*300
else:
	amount = admitdays*250
# print(amount)
# Discount According to
if age>=1 and age<=10:
	TA = 2 / 100 * amount  
elif age>10 and age<26:
	TA = 5 / 100 * amount  
elif age>=26 and age<=50:
	TA = 3 / 100 * amount  
else:
	TA = 7 / 100 * amount  
A = amount-TA
# print(A)
# Discount according to Gender
if gender.lower() == "female":
	TM = 5 / 100 * amount
else:
	TM = 0 / 100 * amount
B = A - TM
# print (B) 
# Tax According to Emloyment  (Enter The Patient Employment (Govt,Pvt,Student,Others) = ")
if employment.lower() == "govt":
	Tax = 10 / 100 * amount
elif employment.lower() == "pvt":
	Tax = 7 / 100 * amount
elif employment.lower() == "student":
	Tax = 5 / 100 * amount
else:
	Tax = 2 / 100 * amount
C = B + Tax
print(f"You Have To Pay Total {C} RS including Tax.")
