#* * * * * 
#*       * 
#*       *
#*       *
#* * * * *

for i in range(1,6):
    for j in range(1,6):
        if(i == 1 or i == 5 or j == 1 or j == 5):
            print('*' , end = ' ')
        else:
            print(' ' , end = ' ')
    print()
print('#############################')

#*
#* *
#*   *
#*     *
#* * * * *

for i in range(1,6):
    for j in range(1,i+1):
        if(j == 1 or i == 5 or i == j ):
            print('*' , end = ' ')
        else:
            print(' ', end = ' ')
    print()
print('############################')

#1 2 3 4 5
#2     5
#3   5
#4 5
#5

for i in range(1,6):
    for j in range(i,6):
        if( i == 1 or j == 5 or i == j):
            print( j , end = ' ')
        else:
            print( ' ', end = ' ')
    print()
print('####################')

#$ $ $ $ $
#* * * * *
#$ $ $ $ $
#* * * * *
#$ $ $ $ $
for i in range(1,6):
    for j in range(1,6):
        if( i %2 ==0  ):
            print( '$' , end = ' ')
        else:
            print( '*', end = ' ')
    print()
print('####################')

for i in range(1,6):
    for j in range(1,6):
        if( i %2 ==0 or j %2 ==0):
            print( '*' , end = ' ')
        else:
            print( '$', end = ' ')
    print()