def sum_Prime(n,sum = 0):
    for i in range(2, n+1):
        if( n%i ==0):
            sum +=i
    return sum
num = int(input("ENTER THE NUMBER : "))
result = sum_Prime(num)
print(f" {num} of the sum of prime number is",result)
    