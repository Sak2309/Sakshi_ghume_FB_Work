n = int(input("enter the no u want separat it : "))
temp = n
while(n != 0):
    d = n % 10
    n = n // 10
    print(f"d ={d}")
    print(f"n ={n}")
