def palindrome_no(n):
    temp = n
    rev =0
    while (temp > 0):
        d1 = temp % 10
        rev = rev *10 +d1
        temp = temp // 10
    if( n == rev):
        return True
    else:
        return False

num = int(input("Enter the number : "))

res = palindrome_no(num)

if palindrome_no(num):
    print(num,"palindrome no.")
else:
    print(num,"is not palindrom.")
