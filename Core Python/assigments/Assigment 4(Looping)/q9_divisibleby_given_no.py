n = int (input("enter the no to divisible by given no. : "))
end = int(input("enter the end range :"))
for i in range(1,end+1):
    if(i %n == 0):
        print(i)