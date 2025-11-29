def power(a,n):
    if(n==0):
        return 1
    return a * power(a,n-1)

def armstrong_sum(num,n):
    if(num==0):
        return 0
    else:
        d= num%10
        return power(d,n) + armstrong_sum(num//10,n)
    
num = int(input("enter the no: "))

count = len(str(num))

res = armstrong_sum(num,count)

if(res == num):
    print(num," is ARMSTRONG ")
else:
    print(num,"NOT armstrong ",)
