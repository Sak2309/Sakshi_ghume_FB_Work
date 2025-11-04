#* 
#* * 
#* * *
#* * * *
#* * * * *

for i in range(1,6):
    for j in range(1, i + 1 ):
        print('*', end = ' ')
    print()

#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

for i in range(1,6):
    for j in range(1, i + 1 ):
        print(i, end = ' ')
    print()
print('########')

#A
#A B
#A B C
#A B C D
#A B C D E
for i in range(1, 6):
    for j in range(1,i+1):
        print( chr(64 + j), end = ' ' )
    print()
    print('####################')
    for i in range(1,6):
        for j in range(65,65+i):
            print(chr(j), end = ' ')
        print()

print('###########################')

#* * * * *
#  * * * *
#    * * *
#      * *
#        *
for i in range(1,6):
    for j in range(1,i):
        print(' ',end = ' ')

    for j in range ( 1, 7-i):
        print('*', end = ' ')
    print()
print('########################')
#        *
#      * *
#    * * *
#  * * * *
#* * * * *
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end = ' ')

    for j in range ( 1, i+1):
        print('*', end = ' ')    
    print()
print('########################')
row =int(input("Enter the row : "))
colum = int(input("Enter the colume : "))
for i in range(1,row):
    for j in range(1,colum +i):
        print(chr(j),end = ' ')
    print()
print('###########################')