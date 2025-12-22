#method 1
from my_packages import chk_function

res = chk_function.chk_even_odd(46)
print(res)

#method 2

from my_packages.chk_function import chk_positive

res =chk_positive(0)
print(res)

#method 3
from my_packages.chk_function import chk_positive,chk_even_odd

even_odd = chk_even_odd(5)
print("even_odd=",even_odd)

pos= chk_positive(7)
print("positive=",pos)
#mehod 4
from my_packages.chk_function import*

even_odd = chk_even_odd(9)
print("even_odd=",even_odd)

pos= chk_positive(79)
print("positive=",pos)

#method 5
from my_packages.chk_function import chk_even_odd as eve_odd
res = eve_odd(4)
print(res)