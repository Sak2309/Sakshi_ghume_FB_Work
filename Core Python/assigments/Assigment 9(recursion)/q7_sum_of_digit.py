def sum_Digit(n):
    if(n <= 0):
        return 0
    else:
        return ( n % 10) + sum_Digit(n //10)
    
n = int(input("Enter the value to separetout and sum : "))
print(sum_Digit(n))
