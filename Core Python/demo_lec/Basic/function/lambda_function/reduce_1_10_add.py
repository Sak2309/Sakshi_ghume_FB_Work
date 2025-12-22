import functools

data = [1,2,3,4,5,6,7,8,9,10]

add =functools.reduce(lambda x , y : x + y ,data)
mul =functools.reduce(lambda x , y : x * y ,data)

print(f'total 1 to 10 = {add} \nmultiplication of 1to 10 = {mul}')