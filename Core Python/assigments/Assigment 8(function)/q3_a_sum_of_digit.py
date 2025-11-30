def sum_Digit(n):
    sum =0
    for i in range(1,n+1):
        sum = sum + i
    return sum
    
n = int(input("ENTER THE NUMBER U HAVE A SUM :"))
print(sum_Digit(n))
