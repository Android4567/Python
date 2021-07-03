# To Calculate The Compound Interest
import math
 
Rate = float(input("Enter The Rate of Interest"))
Time = float(input("Enter the time in years"))
Amount = Principal*(1+Rate/100.0)**Time
CI = Amount-Principal
print("Total amount to be paid is Rs.{}".format(CI)) 
