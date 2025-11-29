def max_min(li):
    max = li[0]
    min = li[0]
    
    for i in range(len(li)):
        if(max < li[i]):
            max = li[i]

        elif(min > li[i]):
            min = li[i]

    return max,min

li=[ 23,67,90,45,22]
max_min_ele= max_min(li)
print("maximum  and minimun no of the list = ",max_min_ele)