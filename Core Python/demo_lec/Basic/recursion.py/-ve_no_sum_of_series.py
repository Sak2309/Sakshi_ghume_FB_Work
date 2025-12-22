def sum_of_serise(n):
    if( n == 0):
        return 0
    elif(n == -1 ):
        return -1
    else:
        return n + sum_of_serise(n + 1)

n = int(input("Enter the sum of series value :"))
print(sum_of_serise(n))
