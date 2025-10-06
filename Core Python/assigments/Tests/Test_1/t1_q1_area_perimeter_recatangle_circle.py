
length = int (input("enter the value os length : "))
breath = int (input("enter the value os breath : "))
r = int (input("enter the value os radius : "))

area_rectangle = length *  breath
perimeter_rectangle = 2 *(length * breath)

area_circle = (3.14 * r * r) 
perimeter_circle = 2 *(3.14 * r)

print(f" area of rectangle {length} , {breath} is {area_rectangle} and peimeter of rectangle is {perimeter_rectangle}")
print(f"area of circle of {r} is {area_circle} and perimeter of circle is {perimeter_circle}")

#enter the value os length : 4
#enter the value os breath : 2
#enter the value os radius : 5
#area of rectangle 4 , 2 is 8 and peimeter of rectangle is 16
#area of circle of 5 is 78.5 and perimeter of circle is 31.400000000000002