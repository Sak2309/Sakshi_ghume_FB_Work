#data should be ascending order
# can't allows duplicate values
def binary_Search(li,ele):
    beg = 0
    end = len(li) - 1
    while( beg <= end ):
        mid = (beg + end ) // 2
    
        if( ele == li[mid] ):
            return mid
    
        elif( ele < li[mid]):
            end = mid - 1

        elif( ele > li[mid]):
            beg = mid + 1
    else:
        return -1

li = [25,26,39,55,70,89]
serach_ele = int(input("ENTER THE VALUE YOU WANT SEARCH : "))
res = binary_Search(li,serach_ele)
print(res)
