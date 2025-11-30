def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact *=i
    return fact
        
num = int (input("ENTER THE NUMBER U HAVE FACTORICAL OF : "))

#result=factorial(num)
#print(result)

print(factorial(num))

