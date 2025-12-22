#method 1
import function

res = function.addition(10,20)
print(res)

sub = function.sub(30,80)
print("subtrction = ",sub)

#method 2
from function import addition

res = addition(40,30)
print(res)

#method 3
from function import addition,sub,multi

add=addition(10,20)
sub=sub(20,40)
mul=multi(20,80)
print(add,sub,mul)

#method 4
from function import *

div= division(10,50)
print(div)

#method 5
from function import addition as add 

res = add(20,40)
print("addition=",res)