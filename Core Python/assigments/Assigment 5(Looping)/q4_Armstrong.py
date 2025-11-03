num = int(input("Enter the number : "))
temp = num
n = len(str(num))
sum = 0
while (num > 0 ):
    digit = num % 10
    print( f"{digit} = ",end =' ')
    sum += digit **n
    print(f"{sum} + ",end =' ')
    num //= 10
    
if( sum == temp):
    print(f"\n {temp} is ARMSTRONG NUMBER.") 
else:
    print(f"{temp} is  not ARMSTRONG NUMBER.")