li =[]
for i in range(1,11):
        li += [i]
print(li)

#even no
li =[]
for i in range(1,11):
    if(i %2 == 0):
        li += [i]
print(li)

#compreshion
li=[i for i in range(1,11)]
print(li)

li=[i for i in range(1,11) if(i % 2 == 0)]
print(li)

li=[[j for j in range(i * 10 + 1,(i + 1 )*10 + 1)] for i in range (0,10) ]
print(li)

