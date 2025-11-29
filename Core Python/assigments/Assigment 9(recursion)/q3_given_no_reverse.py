def reverse_no(n):   
    if(n<=0):
        return 0
    else:
         d = n % 10 
         print(d)
         n = n // 10
    reverse_no(n)
    

num=234
reverse_no(num)