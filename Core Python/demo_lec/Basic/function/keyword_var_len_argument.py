def emp(**data):
    for i in data.items():
        print(i)

emp(id = 101 ,name = 'sakshi')
#('id', 101)
#('name', 'sakshi')
print('##############')
def emp(**data):
    for i,j in data.items():
        print(i,':',j)

emp(id = 101 ,name = 'sakshi')
#id : 101
#name : sakshi
print('#################')
def fun(str,*num,x,y=0):
    print(str)
    print(num)
    print(x)
    print(y)

fun( 'sakshi', 1,2,3,4,5, x=30)
print('###############################')
