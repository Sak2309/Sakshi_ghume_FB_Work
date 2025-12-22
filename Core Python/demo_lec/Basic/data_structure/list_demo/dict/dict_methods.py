#metods :
#1.clear(): show the {} blank 
dict = {1:'java','a':2345,2:'c'}
dict.clear()
print(dict) 
#2.copy : 
dict = {1:'java','a':2345,2:'c'}
dict2 =dict.copy
print(dict2)
print(id(dict2))#diff memory add of dict
dict3=dict
print(id(dict))
print(id(dict3)) #same memroy add of dict
#3.get:
dict = {1:'java','a':2345,2:'c'}
print(dict.get(2)) 
print(dict.get(4)) #none
print(dict.get(4,'key not found'))
#4.items():
print(dict.items())#dict_items([(1, 'java'), ('a', 2345), (2, 'c')])
#5.keys():returns only keys
print(dict.keys())#dict_keys([1, 'a', 2])
#6.values():returns only values
print(dict.values())#dict_values(['java', 2345, 'c'])
#7.pop():
dict = {1:'java','a':2345,2:'c'}
print(dict.pop(2))
#update():
