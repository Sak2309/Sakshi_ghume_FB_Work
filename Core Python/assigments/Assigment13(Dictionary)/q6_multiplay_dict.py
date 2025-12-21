def multi_dict(d):
    res = 1
    for i in d.values():
        res *= i
    
    return res

dict = {'x' : 50, 'y' : 60 }

multi= multi_dict(dict)

print("dictionary : ",dict)
print("multiplication of dictinary : ",multi)