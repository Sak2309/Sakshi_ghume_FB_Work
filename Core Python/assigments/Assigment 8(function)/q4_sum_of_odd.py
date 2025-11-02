def sum_Odd():
    n = int (input("ENTER THE NUMBER : "))
    sum = 0
    for i in range(1,n+1):
        if( i %2 !=0):
            sum += i 
    print(f" sum of odd numbers {n} sum = {sum}")

sum_Odd()