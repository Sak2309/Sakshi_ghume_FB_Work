s1 = int (input(" Enter the 1st side of Triangle : "))
s2 = int (input(" Enter the 2nd side of Triangle : "))
s3 = int (input(" Enter  the  3rd side of Triangle : "))

if((s1+s2) > s3 and (s2+s3) > s1 and (s1+s3) > s2):
    print(f"TRIANGLE IS VAILD.")
else:
    print(f"TRIANGLE IS NOT VAILD.")

#Enter the 1st side of Triangle : 7
 #Enter the 2nd side of Triangle : 10
 #Enter  the  3rd side of Triangle : 5
#TRIANGLE IS VAILD.

# Enter the 1st side of Triangle : 4
 #Enter the 2nd side of Triangle : 3
 #Enter  the  3rd side of Triangle : 7
#TRIANGLE IS NOT VAILD.