def sum_Odd(n):
    sum = 0
    for i in range(1,n+1):
        if( i %2 !=0):
            sum += i 
    return sum
        
n = int (input("ENTER THE NUMBER : "))
print(sum_Odd(n))