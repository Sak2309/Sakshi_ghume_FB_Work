def power(m,n):
    if(n == 0):
        return 1
    else:
        return m * power(m, n - 1)
    
m = int(input("enter the value of base of (m): "))
n= int(input("enter the value of exponnet(n): "))
print(power(m,n))