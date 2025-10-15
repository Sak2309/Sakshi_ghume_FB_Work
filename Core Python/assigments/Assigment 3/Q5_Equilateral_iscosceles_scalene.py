s1 = int(input("enter the side of triangle s1 :"))
s2 = int(input("enter the side of triangle s2 :"))
s3 = int(input("enter the side of triangle s3 :"))

if( s1 == s2 == s3):
    print(f" EQUILLATERAL TRIANGLE.") #all sides of same
elif( s1 == s2 or s2 == s3 or s3 == s1):
    print(f"ISCOSCELESS TRIANGLE.") # 2 sides are same
else:
    print(f"SCALENE TRIANGLE.") # all sides are different
