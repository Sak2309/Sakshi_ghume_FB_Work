n=int(input("ENTER THE VALUE OF NUMBER: "))
print(f"numbers are divisible by 7 and multiple of 5  is : ")
for i in range(1,n+1):
    if(i %7 ==0  and i %5 ==0):
        print(i)