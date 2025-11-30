def sort_by_sec_ele(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size - 1 ):

            if(li[j][1] > li[j + 1][1]):#sec ele compare
                temp=li[j]
                li[j]=li[j+1]
                li[j+1]=temp
    return li

list=[[20,5],[60,1],[30,4],[10,2]]

res = sort_by_sec_ele(list)

print("original list : ",list)
print("sorted list : ",res)