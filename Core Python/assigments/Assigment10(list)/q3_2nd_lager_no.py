def sec_Max(li):
    max = li[0]
    second_Max= 0

    for i in range(len(li)):
        if( max < li[i]):
            second_Max = max
            max = li[i]

        elif(second_Max < li[i]):
            second_Max = li[i]
            
    return second_Max

li = [12,56,78,90,34]
print(sec_Max(li))