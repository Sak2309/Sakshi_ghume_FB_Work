def fact(n):
    if(n<=0):
        return 1
    else:
        return n*fact(n-1)
def sum_serise(n):
    if(n==1):
        return 1
    else:
        return fact(n) + sum_serise(n-1)
    
n = int(input("enter the no : "))
print(sum_serise(n))

#enter the no : 4
#33
#1+2+3+4
#1+2+6+24
#33