def sum_Prime():
    n = int(input("ENTER THE NUMBER : "))
    sum = 0
    for i in range(2, n+1):
        if( n%i ==0):
            sum +=i
    print(f" {n} of the sum of prime number is {sum}")

sum_Prime()
    