def fact(n):
    multi =1
    for i in range (1,n+1):
        multi *= i
    return multi

data = [1,2,3,4,5]
res = list(map (fact,data))
print(res)

#new = fact
#print(new(5))