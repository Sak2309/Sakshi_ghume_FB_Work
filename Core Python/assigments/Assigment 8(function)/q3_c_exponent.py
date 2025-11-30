def exponent(n):
    total =0
    for i in range(1,n+1):
        total += n ** i
    return total
    
num = int(input("ENTER THE NUMBER U HAVE exponent :"))       
print(exponent(num))
