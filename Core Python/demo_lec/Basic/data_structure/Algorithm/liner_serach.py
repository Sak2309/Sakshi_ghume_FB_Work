def liner_serch(li,search):
    for i in range(len(li)):
        if(li[i] == search):
            return i
    else:
        return -1

li = [23,56,78,90,34]
ele=int(input("ENTER THE ELEMENT YOU WANT SEARCH : "))

res=liner_serch(li,ele)
#print(res)

if(res != -1):
    print(f'{ele} is present at index of{res}')
else:
    print(f'{ele} is not present in list')