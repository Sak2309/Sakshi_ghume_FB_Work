def reverse_no():
    
    n= int(input("ENTER THE NUMBER : "))
    rev = 0
    while(n > 0):
        d = n % 10
        rev = rev * 10 + d
        n = n //10
    
    print(f"the reverse number is {rev}")

reverse_no()
