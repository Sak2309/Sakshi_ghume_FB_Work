num = int(input("enter the value of num : "))

temp = num

print(f"before reverse no is {temp}")

d1 = temp % 10
temp = temp // 10
d2 = temp % 10
temp = temp // 10
d3 = temp % 10
temp =temp // 10
#d4 = temp % 10
#temp = temp// 10
#d5 = temp % 10
#temp = temp // 10
#rev = d1 * 10000 + d2 * 1000 + d3 *100 + d4 *10 +d5

rev = d1 * 100 + d2 * 10 + d3

print(f"After reverse no is {rev}")

#enter the value of num1 : 123
#before reverse no is 123
#before reverse no is 321
