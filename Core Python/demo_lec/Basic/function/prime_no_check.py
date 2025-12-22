def prime(n):
    if(n <= 1):
        return False
    for i in range(2,n // 2 +1):
        if (i % n == 0):
            return False
        else:
             return True

num= int(input("ENTER THE NUMBER TO CHECK PRIME OR NOT : "))
print(prime(num))

print('##################################')
def prime(n):
    if(n <= 1):
        return False
    for i in range(2,n // 2 +1):
        if (i % n == 0):
            return False
        else:
             return True

num= int(input("ENTER THE NUMBER TO CHECK PRIME OR NOT : "))
result =prime(num)
if(result):
    print(f'{num} is prime number')
else:
    print(f'{num} is not prime number')
