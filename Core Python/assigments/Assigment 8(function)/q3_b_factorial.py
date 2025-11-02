def factorial():

    n = int (input("ENTER THE NUMBER U HAVE FACTORICAL OF : "))
    fact =1

    for i in range(1,n+1):
        fact *=i
        print(f" FACT OF {n} IS : {i}")
    print(f" FACTORIAL OF {n} IS :{fact}")

factorial()