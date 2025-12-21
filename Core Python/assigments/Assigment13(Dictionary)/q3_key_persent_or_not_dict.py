def chk_dict_key( dict , key):
    
        return key in dict 

di = {'emp_id':101 , 'emp_name':'purva','emp_sal':90000, 'emp_add':'pune'}

key =input("enter the key u want search : ")

res = chk_dict_key(di , key)

if res:
    print("key exists in dictionary..")

else:
    print("key does not exists in dictionary..")