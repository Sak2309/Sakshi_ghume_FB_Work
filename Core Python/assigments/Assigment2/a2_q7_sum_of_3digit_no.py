num = int(input("enter the value of num1 : "))

temp = num

d1 = temp % 10
temp =temp // 10
d2 = temp % 10
temp = temp // 10
d3 = temp % 10
temp = temp // 10

sum = d1 + d2 + d3

print(f"sum of 3 digit no = {sum}")

#enter the value of num1 : 456
#sum of 3 digit no = 15
