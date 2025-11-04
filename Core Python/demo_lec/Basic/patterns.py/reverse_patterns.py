7#5 
#4 5 
#3 4 5
#2 3 4 5
#1 2 3 4 5
for i in range(1,6):
    for j in range(6-i,6):
        print(j, end = ' ')   
    print()
print('###########################')
#1
#2 3
#4 5 6
#7 8 9 10
#111 12 13 14 15
x=1
for i in range(1,6):
    for j in range(1,i+1):
        print(x, end=' ')
        x +=1
    print()
print('############################')
#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1
for i in range(1,7):
    for j in range(1,7-i):
        print(j, end = ' ')   
    print()
print('############################')
#A B C D E
#B C D E
#C D E
#D E
#E
for i in range(1, 6):
    for j in range(64+i,70):
        print( chr(j), end = ' ' )
    print()
print('########################')
for i in range(1,6):
    for j in range(i,6):
        print(j, end = ' ')
    print()
#1 2 3 4 5
#2 3 4 5
#3 4 5
#4 5
#5
