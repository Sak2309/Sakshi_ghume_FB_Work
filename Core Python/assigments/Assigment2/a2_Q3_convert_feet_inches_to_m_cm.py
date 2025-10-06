#enter the values

inches = int(input("Enter the value of inches : "))
feet = int(input("enter the value of feet : " ))

#perfrom opertion

total_inches = (feet * 12 ) + inches 
centimetr = total_inches * 2.54 
meter = centimetr / 100

# Dispaly result

print(f" The total inches of {inches} and {feet} is {total_inches} and centimetr is {centimetr} and meter is {meter}")

#Enter the value of inches : 6
#enter the value of feet : 5
#The total inches of 6 and 5 is 66 and centimetr is 167.64000000000001 and meter is 1.6764000000000001