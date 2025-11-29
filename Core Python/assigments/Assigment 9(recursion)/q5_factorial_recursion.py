def factorial(n):
    if( n == 0):
        return 1
    elif(n < 0):
        return f'{n} ia an negative number.'
    else:
        return n * factorial(n - 1)

num = int(input("Enter the value of factorial : "))
print(factorial(num))  