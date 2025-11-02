def sum_Digit():

    n = int(input("ENTER THE NUMBER U HAVE A SUM :"))
    sum =0

    for i in range(1,n+1):
        sum = sum + i
        print(f"{i}" '+')
    print(f" sum of digit of number {n} is {sum }")

sum_Digit()
