# 1 . pass 

for i in range(1,11):
    pass

# 2. break 
for i in range(1,11):
    if(i == 4):
        break   
    print(i)

# 3. continue
print("//////")
for i in range(1,11):
    if(i == 4):
        continue
    print(i)

# 4. else
print("//////")
for i in range(1,11):
    if(i == 4):
        continue
    print(i)
else:
    print("this is else bolck ")

print("//////")
for i in range(1,11):
    if(i == 4):
        break
    print(i)
else:
    print("this is else bolck ")

print("//////")
for i in range(1,11):
    print(i)
else:
    print("this is else bolck ")

