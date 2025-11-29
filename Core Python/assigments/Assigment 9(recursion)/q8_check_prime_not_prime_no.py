def prime(n,d=2):
    if (n < 2):
        return False
    if(d * d > n):
        return True
    if(n % d == 0):
        return False
    return prime(n,d+1)

n = int(input("Enter the no:"))
print(prime(n))

if(prime(n)):
        print( n,'is prime no')
else:
        print( n,' is not prime')