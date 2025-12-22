def rev(n):
    if (n <= 0):
            pass
    else:
            d = n % 10
            print(d)
            n = n // 10
            rev(n) 

num= int (input("Enter the value to reverse : "))
rev(num)