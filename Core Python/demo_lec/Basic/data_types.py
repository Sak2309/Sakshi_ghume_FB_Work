# memory addresss of variable
x=10
print(id(x))

#simple print value
y=89.4
print(y)

#print which type of data
var =10 +23j
print(type(var))

#text
num="hello world"
num1='good day'
print(type(num))
print(type(num1))

#sequential
#1. list
num=[12,54,9,12]
print(type(num))
print(num)
#2.tuple
num=(12,54,9,12)
print(type(num))
print(num)

#set type
#1.set
num={12,54,9,12}
print(type(num))
print(num)
#2.frozenset
num=frozenset({12,54,9,12})
print(type(num))
print(num)

#mapping
#1.dict
var={'id': 121,'name':'sakshi','add':'pune'}
print(type(var))
print(var)

#Boolean
#1.True
var=True 
print(type(var))
print(var)

#2.False
var=False
print(type(var))
print(var)

#None type
#1.None
var=None
print(type(var))
print(var)