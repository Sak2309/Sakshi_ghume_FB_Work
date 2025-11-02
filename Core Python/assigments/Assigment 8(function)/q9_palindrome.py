def palindrome_no():
    n = int(input("Enter the number : "))
    temp = n
    rev =0
    while (temp > 0):
        d1 = temp % 10
        rev = rev *10 +d1
        temp = temp // 10
    
    if( n == rev):
        print(f"{n}IS PALINDER NUMBER.")
    else:
        print(f"{n} IS NOT PALINDER NUMBER.")

palindrome_no()