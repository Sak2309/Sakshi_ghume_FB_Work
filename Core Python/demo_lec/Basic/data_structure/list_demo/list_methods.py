#methods of list

#1. append = add element at the end 
li = [40,30,20,10]
li.append(50)
print(li)

#2. copy
li2 = li.copy()
print(li2)
li3 = li
print(id(li))# same memory address li and li3
print(id(li2)) #diff memory address li2 because he copy the data li 
print(id(li3)) #same memory address li and li3 because = to sign  
print(li3)

#3.count = cont occurance of given element. 
print(li.count(10)) # HOW many times element are present in list or li

#4.extend = add multiple elements in the end of list or li
li.extend([60,70,80,90])
print(li)

#5.index = return index value present ,otherwise given value
print(li.index(70)) # index 6
#print(li.index(100)) # ValueError: 100 is not in list

#6.insert = add element at given index . shift the elements right side
#li = [10,30,40,60,70]
li.insert(2,101)
print(li)

#7.pop() = remove element given index
li.pop(1)
print(li) # remove index 1 value

#8.remove = element are remove
li.remove(20)
print(li)

#9. reverse = the list are reverse order
li.reverse()
print(li)

#10. sort() = sequancely arrange all element
li.sort()
print(li)

#11.clear =list remove or clear all elements in given list or li
li = [10,20,49,67]
li.clear()
print(li)