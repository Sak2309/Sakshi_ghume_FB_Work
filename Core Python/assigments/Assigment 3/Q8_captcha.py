u_id = (input("Enter the USERNAME : "))
u_pass = (input("Enter the PASSWORD : "))
id = 'sakshighume2309@gmail.com'
password = 'sakshi#23'
capta = 2367
if( u_id == id and u_pass == password):
    print(f"LOGIN SUCESFULL.")
    print(capta)
    capta_23 = int(input("Enter the CAPTCH : "))
    if(capta == capta_23):
        print("SUCESSFULL")
    else:
        print("INVAILD CAPTA.")
else:
    print("Try agin ! USER PASSWORD AND ID IS NOT VAILD.")
#Enter the USERNAME : sakshighume2309@gmail.com
#Enter the PASSWORD : sakshi#23
#LOGIN SUCESFULL.
#2367
#Enter the CAPTCH : 2367
#SUCESSFULL