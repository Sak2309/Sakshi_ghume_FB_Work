def selection_Sort(li):
    size = len(li)
    for i in range(0 , size):
        min = i
        for j in range(i + 1 , size):
            
            if(li[min] > li[j]):
                min = j
        li[i] , li[min] = li[min] , li[i]
        print(li)
    return li

li = [70,60,20,30,10]
print("BEFORE SORTING : ", li)
li = selection_Sort(li)
print("AFTER SORTING : ", li) 