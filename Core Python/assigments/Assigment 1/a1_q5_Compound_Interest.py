#Enter the values

p=int(input("Enter the value of Principal Amount is : "))
r=int(input("Enter the value of Reat Amount is : "))
t=int(input("Enter the value of Time is : "))

#perform opertion

ci = p * (1 + r/100) * t - p

#Display result

print(f"The Compound interest of {p},{r},{t} is :  {ci}")

#Enter the value of Principal Amount is : 750000
#Enter the value of Reat Amount is : 12
#Enter the value of Time is : 5
#The Compound interest of 750000,12,5 is :  3450000.000000001