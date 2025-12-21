def squr(n):
    dict = {}

    for i in range(1,n+1):
    
        dict[i]=i*i

    return dict

n =int(input("enter the no : "))

print(squr(n))