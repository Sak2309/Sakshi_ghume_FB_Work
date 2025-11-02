n = int(input("Enter the value to cheak prime or not prime no. : "))

for i in range(2,n):
    if(n % i == 0):
        print(i)
        print(f"{n} is a not prime no. ")
        break
else:
    print(f"{n} is a prime no.")