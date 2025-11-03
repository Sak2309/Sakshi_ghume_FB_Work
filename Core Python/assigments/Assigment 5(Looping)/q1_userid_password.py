u_id = "admin"
paas = "123"

for  i in range(1,4):
    user_id = input("ENTER THE USER ID : ")
    pwd = input("ENTER THE PASSWORD : ")

    if( u_id == user_id and paas == pwd):
        print("LOGIN SUCCESSFUL ")
        break
    else:
        print("INCORRECT USER ID AND PASSWORD ")
    if (i <= 3):
        print("TRY AGAIN !!!!")
else:
     print("ACCESS DENIED AND 2 ATTEMTS FAILED !!!!")
    