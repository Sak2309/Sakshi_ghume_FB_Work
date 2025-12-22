def memorization(fun):
    cache ={}
    def warpper(n):
        if(n in cache):
            print(" output is avilable..")
            return cache[n]
        output=fun(n)
        cache[n]=output
        print("output not avilable..")
        return output
    return warpper

@memorization
def fact(n):
    f=1
    for i in range(1,n+1):
        f*= i
    return f

res=fact(5)
print(f'fact of 5 is',res)
print('################')
res=fact(5)
print(res)
print('################')
res=fact(4)
print(res)
#o/p:
#output not avilable..
#120
################
 #output is avilable..
#120
################
#output not avilable..
#24