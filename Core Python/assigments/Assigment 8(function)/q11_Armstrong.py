def armstrong_no(n):
    temp=n
    count= len(str(n))
    sum = 0
    while (n > 0 ):
        digit = n % 10
        sum += digit ** count
        n //= 10
        
    if (sum == temp):
          return True
    else:
          return False        
num = int(input("Enter the number : "))

res=armstrong_no(num)

if( armstrong_no(num)):
    print(res,"is ARMSTRONG NUMBER.")
else:
    print(res," is not ARMSTRONG NUMBER.")