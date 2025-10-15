age_m =int(input("enter the age of male : "))
age_f =int(input("enter the age of female : "))

if( age_m >=21 and age_f >=18 ):
    print(f"both male and female eligible to get  marry")
if(age_m !=21 and  age_f >=18 ):
    print("male is not eligible to get marray but feamle is get to marray ")

elif(age_f != 18 and age_m >=21):
    print("male is eligible to get marray but feamle is not get to marray ")

else:
    print(f" both the  of male and femal not eligibale to get marray")