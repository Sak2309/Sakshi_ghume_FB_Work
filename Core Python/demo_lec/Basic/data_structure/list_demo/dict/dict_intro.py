#1.structure : {} key:value
dict = {1:'java','a':2345,2:'c'}

#2.type of data =hetrogenous
print(dict)

#3.sequance: orderd collection
#4.changle : key : immutable, value : mutable
# we used dict iteam to search a value of it not using index
dict['a']= 999
print(dict) #we can change the values of iteam but not change key

dict['b']=1234
print(dict)  # the iteam is not present in dict they add it in dict 

dict={(1,2,3):'1st value'}
print(dict)

dict={[1,3,4]:'2nd value'} #list are not used in dict get unhashable type
print(dict)