def Concate(dict1,dict2):
    dict1.update(dict2)
    return dict1
    
    #retyrun dict1 | dict2
    
di1 ={'emp_id':101 , 'emp_name':'purva'}
di2 ={'emp_sal':90000, 'emp_add':'pune'}

res = Concate(di1 , di2)

print("dictionary 1 : ",di1)
print("dictionary 2 : ",di2)
print("concation dictionary  : ",res)


