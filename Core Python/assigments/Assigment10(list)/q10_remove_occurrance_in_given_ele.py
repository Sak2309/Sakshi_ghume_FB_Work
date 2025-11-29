def remove_Occurance(original_li,ele):
    li=[]

    for i in original_li:
        if (i != ele):
            li.append(i)
    return li

n=[25,10,25,40,25,50]
print("original list:",n)
val = int(input("enter the value to be remove : "))

res= remove_Occurance(n,val)
print("removing of occurance no",val,":",res)