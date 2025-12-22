def fact(num):
    if(num==0):
        return 1
    else:
        return num * fact ( num-1)
    
def strong(num):
    if ( num <= 0):
        return 0
    else:
        d = num % 10
        f = fact(d)
        return f + strong(num // 10)
    
def check_Strong(num):
    if(num == strong(num)):#strong(num)=recursion function
        return f'{num} IS A STRONG NUMBER'
    else:
        return f'{num} IS NOT A STRONG NUMBER'

n = int(input("enter the number to check the strong or not :"))
print(check_Strong(n))