def chk_dict_key( dict , key):

    if key in dict:
        dict.pop(key) 
        return True
    
    else:
        return False 

di = {'emp_id':101 , 'emp_name':'purva','emp_sal':90000, 'emp_add':'pune','emp_dept': 'Admin'}

key =input("enter the key u want delet/remove it : ")

print("original dictionary : ",di)
res = chk_dict_key(di , key)

if res:
    print("key remove from dictionary successfully......")

else:
    print("key does not remove from dictionary.. try agin ....!")

print("dictionary : ",di)