def range_fun(start ,stop,step =1):
    current = start 
    if (step > 0):
        while (current < stop):
            yield current
            current += step
    elif (step  < 0):
        while (current > stop):
            yield current
            current += step
    else:
         raise ValueError("step cannot be zero")
    
for i in range_fun(2,10,2):
    print(i)
print("reverse : ")
for i in range_fun(10,0,-3):
    print(i)

