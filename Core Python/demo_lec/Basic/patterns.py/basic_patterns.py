# * 
# * 
# * 
# * 
# *
for i in range(1,6):
    print(f" * " )
print('############################')

# ***** 

for i in range(1,6):
   print(f" * " , end = ' ')
print()
print('############################')

# *****
# *****
# *****
# *****
# *****
for i in range(1, 6):
    for j in range(1, 6):
        print('*', end = ' ')
    print()
print('########################')

for i in range(1, 6):
    for j in range(1, 8):
        print('*', end = ' ')
    print()
print('########################')

#1 1 1 1 1 
#2 2 2 2 2
#3 3 3 3 3
#4 4 4 4 4 
#5 5 5 5 5

for i in range(1, 6):
    for j in range(1, 6):
        print( i, end = ' ')
    print()
print('########################')

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, 6):
        print( j, end = ' ')
    print()
print('########################')

#a a a a a
#b b b b b
#c c c c c
#d d d d d
#e e e e e

for i in range(1, 6):
    for j in range(1, 6):
        print( chr(64 +i), end = ' ' )
    print()
print('########################')

# a b c d e
# a b c d e
# a b c d e
# a b c d e
# a b c d e

for i in range(1, 6):
    for j in range(1, 6):
        print( chr(64 +j), end = ' ' )
    print()
print('########################')

