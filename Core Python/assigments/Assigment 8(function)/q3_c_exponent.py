def exponent():

    n = int(input("ENTER THE NUMBER U HAVE exponent :"))
    total =0

    for i in range(1,n+1):
        total += n** i
        print(f"EXPONENT = {i} of {n}")

    print(f" EXPONTN OF {n} IS :{total}")
    
exponent()
