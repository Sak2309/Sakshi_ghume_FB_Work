#dispaly 1 yo 10
for i in range(1,11):
    print(i,'\n')
#display  4 table 

for i in range(4,41,4):
    print(i)

#display n no of multipilcation table

n = int(input("Enter the number of multiplication : "))
for i in range(n, n*10+1, n):
    print(i)

#display n no of multipilcation table reverse

n = int(input("Enter the number of multiplication : "))
for i in range( n*10,n-1, -n):
    print(i)



