def bubble_Sort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size - 1 ):

            if(li[j] > li[j + 1]):
                li[j] , li[j + 1] = li[j + 1] , li[j]
            print(li)

    return li
li = [60,40,30,20,10]
print("BEFORE SORTING : ", li)
li = bubble_Sort(li)
print("AFTER SORTING : ", li)