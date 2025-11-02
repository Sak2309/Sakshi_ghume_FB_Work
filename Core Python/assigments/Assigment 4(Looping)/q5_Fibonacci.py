num = int(input("Enter the number : "))
n1 =0
n2 = 1
sum =0
for i in range(0, num+1):
    n1 = n2
    n2= sum
    sum =n1+n2
    print(sum)
print()
