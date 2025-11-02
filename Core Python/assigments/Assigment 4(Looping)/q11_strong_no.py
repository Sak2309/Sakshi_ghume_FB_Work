n = int (input("ENTER THE NUMBER TO CHRCK STRONG NUMBER OR NOT : "))
temp =n
sum =0
while(n > 0):
    d = n % 10
    fact = 1
    for i in range(1,d +1):
        fact = fact * i

    sum = sum + fact
    n = n // 10
if ( sum == temp):
    print(f"{temp} is strong number ")
else:
    print(f"{temp} is strong number ")