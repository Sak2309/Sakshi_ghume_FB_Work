def fibonacci(n):
    n1 =0
    n2 = 1
    sum =0
    for i in range(num+1):
        n1 = n2
        n2= sum
        sum =n1+n2
    return sum
    
num = int(input("Enter the number : "))
print(fibonacci(num))
