def armstrong_no():
    num = int(input("Enter the number : "))
    temp = num
    n = len(str(num))
    sum = 0
    while (num > 0 ):
        digit = num % 10
        sum += digit ** n
        num //= 10
    if( sum == temp):
        print(f"{temp} is ARMSTRONG NUMBER.") 
    else:
        print(f"{temp} is  not ARMSTRONG NUMBER.")
armstrong_no()